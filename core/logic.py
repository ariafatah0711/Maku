import time
from .models import Transaction
from .inputValidate import inputValidate
from .utils import *

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
        """List all transactions from the file CSV or Excel."""
        time.sleep(0.3)
        transactions = self.data.read()

        show_header("List of Transactions")
        show_list_transaction(transactions)

        input("\n[O] Press Enter to return to the main menu... ")
        time.sleep(0.3)

    def add_transaction(self):
        """Add a new transaction to the file CSV or Excel."""
        transactions = self.data.read()
        new_id = max([int(t.id) for t in transactions] + [0]) + 1
        ErrorText = inputValidate()

        try:
            while True:
                date = ErrorText.date("[?] Date (YYYY-MM-DD) (or 'now') \t\t: ")
                type = ErrorText.type("[?] Type (Income/Expense) (or 'I' / 'E') \t: ")
                category = input("[?] Category (Optional) \t\t\t: ")
                amount = ErrorText.float("[?] Amount \t\t\t\t\t: ")
                note = input("[?] Note (Optional) \t\t\t\t: ")

                transaction = Transaction(new_id, date, type, category, amount, note)
                self.data.write(transaction)

                print("\n[✔] Transaction added successfully")
                time.sleep(1)
                break
        except KeyboardInterrupt:
            # User pressed Ctrl+C while entering fields — cancel add and return
            print("\n[!] Add cancelled, returning to main menu...")
            time.sleep(1)
            return

    def delete_transaction(self):
        """Delete a transaction from the file CSV or Excel by its ID."""
        time.sleep(0.3)
        transactions = self.data.read()

        show_header("List of Transactions")
        show_list_transaction(transactions)
        del_id = input("[?] Enter Transaction ID to delete: ")
        self.data.delete(del_id)

        print("\n[✔] Transaction deleted successfully")
        time.sleep(1)

    def edit_transaction(self):
        """Edit an existing transaction in the file CSV or Excel."""
        pass
