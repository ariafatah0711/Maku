import time
import os
from datetime import datetime
from .models import Transaction
from .utils import *
from cli import inputValidate

from .handlers import CSVHandler, ExcelHandler

class TransactionLogic():
    mode = 'excel'  # default mode

    def __init__(self, file_path, mode='excel'):
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

    def export_transactions(self, export_dir='exports'):
        """Export all transactions to an Excel file under `export_dir`.

        The exported filename is generated as `YYYY-MM-DD_HHMMSS.xlsx` and the
        function returns the full path to the created file.
        """
        transactions = self.data.read()

        # Ensure export directory exists
        try:
            os.makedirs(export_dir, exist_ok=True)
        except PermissionError:
            raise PermissionError(f"[!] Permission denied creating export directory: {export_dir}")

        filename = datetime.now().strftime('%Y-%m-%d_%H%M%S.xlsx')
        export_path = os.path.join(export_dir, filename)

        # Always export to Excel
        export_handler = ExcelHandler(export_path)

        for t in transactions:
            export_handler.write(t)

        return export_path
