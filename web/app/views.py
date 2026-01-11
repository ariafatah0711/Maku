from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from core import TransactionLogic, ReadAllConfig
import os

CONFIG = ReadAllConfig()
file_path = CONFIG["FILE_EXCEL"]
export_dir = str(CONFIG.get("EXPORT_DIR", "exports"))

def get_logic():
    return TransactionLogic(file_path, "excel")

def app(request):
    logic = get_logic()

    if request.method == "POST":
        logic.add_transaction(
            date=request.POST["date"],
            type=request.POST["type"],
            category=request.POST.get("category", ""),
            amount=request.POST["amount"],
            note=request.POST.get("note", ""),
        )
        return redirect("app:app")

    transactions = list(reversed(logic.list_transactions()))
    totals = logic.get_totals()
    return render(request, "app.html", {"transactions": transactions, "totals": totals})

def export_transactions(request):
    logic = get_logic()

    try:
        export_path = logic.export_transactions(export_dir)
    except Exception as e:
        return render(request, "app/app.html", {"transactions": logic.list_transactions(), "error": str(e)})

    if os.path.exists(export_path):
        try:
            return FileResponse(open(export_path, "rb"), as_attachment=True, filename=os.path.basename(export_path))
        except Exception:
            raise Http404("Could not open exported file")
    else:
        raise Http404("Exported file not found")

def edit_transaction(request, transaction_id):
    logic = get_logic()
    transactions = logic.list_transactions()

    transaction = next(
        (t for t in transactions if str(t.id) == str(transaction_id)),
        None
    )

    if not transaction:
        return redirect("app:app")

    if request.method == "POST":
        logic.edit_transaction(
            transaction_id=transaction_id,
            date=request.POST["date"],
            type=request.POST["type"],
            category=request.POST.get("category", ""),
            amount=request.POST["amount"],
            note=request.POST.get("note", ""),
        )
        return redirect("app:app")

    return render(request, "edit.html", {"transaction": transaction})

def delete_transaction(request, transaction_id):
    logic = get_logic()
    logic.delete_transaction(transaction_id)
    return redirect("app:app")
