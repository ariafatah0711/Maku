import sys, os
import pandas as pd

# add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core import Transaction, ReadConfig

HEADERS = ['id', 'tanggal', 'jenis', 'kategori', 'jumlah', 'catatan']
def _ensure_excel(path):
    if not os.path.exists(path):
        pd.DataFrame(columns=HEADERS).to_excel(path, index=False)

def read_excel(file_path):
    _ensure_excel(file_path)
    df = pd.read_excel(file_path)
    transactions = []
    for _, row in df.iterrows():
        transactions.append(Transaction(
            id=row.get('id'),
            date=row.get('tanggal'),
            type=row.get('jenis'),
            category=row.get('kategori'),
            amount=float(row.get('jumlah', 0) or 0),
            note=row.get('catatan') or ''
        ))
    return transactions

def write_excel(file_path, id, date, type, category, amount, note):
    _ensure_excel(file_path)
    df = pd.read_excel(file_path)
    df = pd.concat([df, pd.DataFrame([{
        'id': id,
        'tanggal': date,
        'jenis': type,
        'kategori': category,
        'jumlah': amount,
        'catatan': note
    }])], ignore_index=True)
    df.to_excel(file_path, index=False)

def delete_excel(file_path, id):
    _ensure_excel(file_path)
    df = pd.read_excel(file_path)
    df = df[df['id'].astype(str) != str(id)].reset_index(drop=True)
    # Renumber ids to be sequential starting at 1
    if 'id' in df.columns:
        df['id'] = list(range(1, len(df) + 1))
    df.to_excel(file_path, index=False)

def update_excel(file_path, id, date, type, category, amount, note):
    _ensure_excel(file_path)
    df = pd.read_excel(file_path)
    df.loc[df['id'].astype(str) == str(id), ['tanggal', 'jenis', 'kategori', 'jumlah', 'catatan']] = [
        date, type, category, amount, note
    ]
    df.to_excel(file_path, index=False)

def show_list_transaction(transactions):
    for t in transactions:
        print(f"ID: {t.id}, Date: {t.date}, Type: {t.type}, Category: {t.category}, Amount: {t.amount}, Note: {t.note}")

if __name__ == "__main__":
    __FILE_PATH__ = ReadConfig('FILE_EXCEL')

    print("[+] Before Write")
    txs = read_excel(__FILE_PATH__); show_list_transaction(txs)

    print("\n[+] Write Data Excel - ID 999")
    write_excel(__FILE_PATH__, 999, '2024-01-01', 'income', 'salary', 5000.0, 'January salary note')

    print("\n[+] After Write")
    txs = read_excel(__FILE_PATH__); show_list_transaction(txs)

    print("\n[+] Delete Data Excel - ID 999")
    delete_excel(__FILE_PATH__, 999)

    update_excel(__FILE_PATH__, 1, '2024-02-02', 'expense', 'groceries', 150.0, 'February groceries note')

    print("\n[+] After Delete And Update - ID 1")
    txs = read_excel(__FILE_PATH__); show_list_transaction(txs)
