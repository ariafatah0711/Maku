import sys, os
import csv

# add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import Transaction, ReadConfig, transaction_to_dict, show_list_transaction

FIELD_NAMES = ['id', 'tanggal', 'jenis', 'kategori', 'jumlah', 'catatan']

# CLASS CSVHandler
class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return [
                Transaction(
                    id=row['id'], date=row['tanggal'],
                    type=row['jenis'], category=row['kategori'],
                    amount=float(row['jumlah']), note=row['catatan']
                ) for row in reader
            ]

    def write(self, transaction):
        with open(file=self.file_path, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
            writer.writerow(transaction_to_dict(transaction))

    def delete(self, id):
        transactions = self.read()
        filtered = [
            t for t in transactions
                if str(t.id) != str(id)
        ]

        # Renumber IDs sequentially so file keeps contiguous ids starting at 1
        for idx, t in enumerate(filtered, start=1):
            try:
                t.id = idx
            except Exception:
                pass

        with open(self.file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
            writer.writeheader()
            for t in filtered:
                writer.writerow(transaction_to_dict(t))

    def update(self, transaction):
        transactions = self.read()
        updated = []
        for t in transactions:
            if str(t.id) == str(transaction.id):
                t.date = transaction.date
                t.type = transaction.type
                t.category = transaction.category
                t.amount = transaction.amount
                t.note = transaction.note
            updated.append(t)

        with open(self.file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
            writer.writeheader()
            for t in updated: writer.writerow(transaction_to_dict(t))

if __name__ == "__main__":
    __FILE_PATH__ = ReadConfig('FILE_CSV')
    csv_data = CSVHandler(__FILE_PATH__)

    # [01] Testing Read CSV
    print("[+] Before Write"); transactions = csv_data.read(); show_list_transaction(transactions)

    # [02] Testing Write CSV
    print("\n[+] Write Data CSV - ID 999"); csv_data.write(Transaction(999, '2024-01-01', 'income', 'salary', 5000.0, 'January salary note'))
    # [03] Read again after write
    transactions = csv_data.read(); show_list_transaction(transactions)

    # [04] Testing Delete CSV
    print("\n[+] Delete Data CSV - ID 999"); csv_data.delete(999)
    # [05] Read again after delete
    transactions = csv_data.read(); show_list_transaction(transactions)

    # [06] Testing Update CSV
    print("\n[+] Update Data CSV - ID 1"); csv_data.update(Transaction(1, '2024-02-01', 'expense', 'groceries', 150.0, 'February groceries note'))
    # [07] Read again after update
    transactions = csv_data.read(); show_list_transaction(transactions)
