import os

def show_header(title):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 80)
    print(f"{title.center(80)}")
    print("=" * 80)

def show_main_menu():
    print("[01] View Transactions")
    print("[02] Add Transaction")
    print("[03] Update Transaction")
    print("[04] Delete Transaction")
    print("[05] Export Transactions")

# Menampilkan daftar transaksi dalam format tabel
def show_list_transaction(transactions):
    if not transactions:
        print("No transactions available.")
        return

    # Header tabel
    headers = ['ID', 'Tanggal', 'Jenis', 'Kategori', 'Jumlah', 'Catatan']
    col_widths = [5, 12, 10, 15, 10, 25]  # total ±77
    header_line = "".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    print(header_line)
    print("-" * 80)

    # Isi tabel
    for t in transactions:
        print(f"{t.id:<5}{t.date:<12}{t.type:<10}{t.category:<15}{t.amount:<10}{t.note:<25}")
    print("-" * 80)
