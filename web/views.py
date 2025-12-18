from django.shortcuts import render, redirect
from core import TransactionLogic
from utils import ReadAllConfig

CONFIG = ReadAllConfig()
mode = str(CONFIG["MODE"])
file_path = CONFIG["FILE_CSV"] if mode == "csv" else CONFIG["FILE_EXCEL"]

def get_logic():
    return TransactionLogic(file_path, mode)

def index(request):
    logic = get_logic()

    if request.method == "POST":
        logic.add_transaction(
            date=request.POST["date"],
            type=request.POST["type"],
            category=request.POST.get("category", ""),
            amount=request.POST["amount"],
            note=request.POST.get("note", ""),
        )
        return redirect("home")

    transactions = logic.list_transactions()
    return render(request, "index.html", {"transactions": transactions})

def edit_transaction(request, transaction_id):
    logic = get_logic()
    transactions = logic.list_transactions()

    transaction = next(
        (t for t in transactions if str(t.id) == str(transaction_id)),
        None
    )

    if not transaction:
        return redirect("home")

    if request.method == "POST":
        logic.edit_transaction(
            transaction_id=transaction_id,
            date=request.POST["date"],
            type=request.POST["type"],
            category=request.POST.get("category", ""),
            amount=request.POST["amount"],
            note=request.POST.get("note", ""),
        )
        return redirect("home")

    return render(request, "edit.html", {"transaction": transaction})

def delete_transaction(request, transaction_id):
    logic = get_logic()
    logic.delete_transaction(transaction_id)
    return redirect("home")
