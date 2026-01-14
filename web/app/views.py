from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from core import TransactionLogic, ReadAllConfig
from datetime import datetime
import os

CONFIG = ReadAllConfig()
file_path = CONFIG["FILE_EXCEL"]
export_dir = str(CONFIG.get("EXPORT_DIR", "exports"))

def get_logic():
    return TransactionLogic(file_path, "excel")

def format_transaction(transaction):
    """Format transaction data for display"""
    try:
        # Try to parse date if it's a string
        if isinstance(transaction.date, str):
            date_obj = datetime.strptime(transaction.date, '%Y-%m-%d')
            transaction.date_formatted = date_obj.strftime('%d %b %Y')
        else:
            transaction.date_formatted = transaction.date.strftime('%d %b %Y')
    except:
        transaction.date_formatted = transaction.date
    return transaction

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

    transactions = [format_transaction(t) for t in reversed(logic.list_transactions())]
    totals = logic.get_totals()
    return render(request, "app.html", {"transactions": transactions, "totals": totals})

def export_transactions(request):
    logic = get_logic()

    try:
        export_path = logic.export_transactions(export_dir)
    except Exception as e:
        transactions = [format_transaction(t) for t in reversed(logic.list_transactions())]
        return render(request, "app.html", {"transactions": transactions, "totals": logic.get_totals(), "error": str(e)})

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
