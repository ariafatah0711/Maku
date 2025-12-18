import time
from .models import Transaction
from .util import *
from utils import inputValidate

from handlers.csv_handler import CSVHandler
from handlers.excel_handler import ExcelHandler

class TransactionLogic():
    mode = 'csv'  # default mode

    def __init__(self, file_path, mode='csv'):
        self.mode = mode
        if mode == 'csv':
            self.data = CSVHandler(file_path)
        elif mode == 'excel':
            self.data = ExcelHandler(file_path)
        else:
            raise ValueError(f"Unsupported mode: {mode}")

    def list_transactions(self):
        """Return all transactions from the file CSV or Excel."""
        return self.data.read()

    def add_transaction(self, date, type, category, amount, note):
        """Add a new transaction to the file CSV or Excel. All fields must be provided."""
        transactions = self.data.read()
        new_id = max([int(t.id) for t in transactions] + [0]) + 1
        transaction = Transaction(new_id, date, type, category, amount, note)
        self.data.write(transaction)
        return transaction

    def delete_transaction(self, transaction_id):
        """Delete a transaction from the file CSV or Excel by its ID."""
        self.data.delete(transaction_id)
        return True

    def edit_transaction(self, transaction_id, date=None, type=None, category=None, amount=None, note=None):
        """Edit an existing transaction in the file CSV or Excel. Only provided fields will be updated."""
        transactions = self.data.read()
        updated = False
        for t in transactions:
            if str(t.id) == str(transaction_id):
                if date is not None: t.date = date
                if type is not None: t.type = type
                if category is not None: t.category = category
                if amount is not None: t.amount = amount
                if note is not None: t.note = note

                updated = True
                # After updating, call the handler's update method for this transaction
                self.data.update(t)
                break
        if updated:
            return True
        else:
            raise ValueError(f"Transaction with ID {transaction_id} not found.")
