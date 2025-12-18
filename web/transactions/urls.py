from django.urls import path
from .views import transactions, transaction_detail

urlpatterns = [
    path("transactions/", transactions),
    path("transactions/<int:tx_id>/", transaction_detail),
]
