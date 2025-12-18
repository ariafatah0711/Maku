import json
from django.http import JsonResponse, HttpResponseNotAllowed
from core import TransactionLogic
from utils import ReadAllConfig

CONFIG = ReadAllConfig()
mode = str(CONFIG["MODE"])
file_path = CONFIG["FILE_CSV"] if mode == "csv" else CONFIG["FILE_EXCEL"]

logic = TransactionLogic(file_path, mode)

# =====================
# API Views
# =====================
# GET + POST
def transactions(request):
    if request.method == "GET":
        data = [
            {
                "id": t.id,
                "date": t.date,
                "type": t.type,
                "category": t.category,
                "amount": t.amount,
                "note": t.note,
            }
            for t in logic.list_transactions()
        ]
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        body = json.loads(request.body)

        tx = logic.add_transaction(
            date=body["date"],
            type=body["type"],
            category=body.get("category", ""),
            amount=body["amount"],
            note=body.get("note", ""),
        )

        return JsonResponse(
            {"message": "created", "id": tx.id},
            status=201
        )

    return HttpResponseNotAllowed(["GET", "POST"])


# PUT + DELETE
def transaction_detail(request, tx_id):
    if request.method == "PUT":
        body = json.loads(request.body)
        logic.edit_transaction(tx_id, **body)
        return JsonResponse({"message": "updated"})

    elif request.method == "DELETE":
        logic.delete_transaction(tx_id)
        return JsonResponse({"message": "deleted"})

    return HttpResponseNotAllowed(["PUT", "DELETE"])
