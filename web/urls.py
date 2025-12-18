from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("delete/<int:transaction_id>/", delete_transaction, name="delete"),
    path("edit/<int:transaction_id>/", edit_transaction, name="edit"),
]
