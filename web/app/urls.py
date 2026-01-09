from django.urls import path
from .views import app, edit_transaction, delete_transaction, export_transactions

app_name = "app"

urlpatterns = [
    path("", app, name="app"),
    path("edit/<int:transaction_id>/", edit_transaction, name="edit"),
    path("delete/<int:transaction_id>/", delete_transaction, name="delete"),
    path("export/", export_transactions, name="export"),
]
