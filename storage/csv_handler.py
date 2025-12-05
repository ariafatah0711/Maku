import sys, os
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import Transaction, ReadConfig

def read_csv(file_path):
    transactions = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Transaction_obj = Transaction(
                id=row['id'],
                date=row['tanggal'],
                type=row['jenis'],
                category=row['kategori'],
                amount=float(row['jumlah']),
                note=row['catatan']
            )
            transactions.append(Transaction_obj)

    return transactions

def write_csv(file_path, id, date, type, category, amount, note):
    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'tanggal', 'jenis', 'kategori', 'jumlah', 'catatan']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({
            'id': id,
            'tanggal': date,
            'jenis': type,
            'kategori': category,
            'jumlah': amount,
            'catatan': note
        })

def delete_csv(file_path, id):
    transactions = read_csv(file_path)
    filtered = [
        t for t in transactions
            if str(t.id) != str(id)
    ]

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'tanggal', 'jenis', 'kategori', 'jumlah', 'catatan']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for t in filtered:
            writer.writerow({
                'id': t.id,
                'tanggal': t.date,
                'jenis': t.type,
                'kategori': t.category,
                'jumlah': t.amount,
                'catatan': t.note
            })

def show_list(transactions):
    for t in transactions:
        print(f"ID: {t.id}, Date: {t.date}, Type: {t.type}, Category: {t.category}, Amount: {t.amount}, Note: {t.note}")

if __name__ == "__main__":
    __FILE_PATH__ = ReadConfig('FILE_CSV')
    transactions = read_csv(__FILE_PATH__)

    # [01] Testing Read CSV
    print("[+] Before Write")
    show_list(transactions)

    # [02] Testing Write CSV
    print("\n[+] Write Data CSV - ID 999")
    write_csv(__FILE_PATH__, 999, '2024-01-01', 'income', 'salary', 5000.0, 'January salary note')

    # [03] Read again after write
    print("\n[+] After Write")
    transactions = read_csv(__FILE_PATH__); show_list(transactions)

    # [04] Testing Delete CSV
    print("\n[+] Delete Data CSV - ID 999")
    delete_csv(__FILE_PATH__, 999)

    # [05] Read again after delete
    print("\n[+] After Delete")
    transactions = read_csv(__FILE_PATH__); show_list(transactions)
