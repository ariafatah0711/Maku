import os

def show_header(title):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 85)
    print(f"{title.center(85)}")
    print("=" * 85)

def show_main_menu():
    print("[01] View Transactions")
    print("[02] Add Transaction")
    print("[03] Update Transaction")
    print("[04] Delete Transaction")
    print("[05] Export Transactions")

def show_summary(totals):
    """Display summary with totals."""
    print("\n" + "=" * 85)
    print("SUMMARY".center(85))
    print("=" * 85)

    def format_rupiah(amount):
        try:
            amt = float(amount)
        except Exception:
            return str(amount)
        return "Rp {:,.0f}".format(amt).replace(",", ".")

    print(f"Total Pemasukan (Income)   : {format_rupiah(totals['total_income'])}")
    print(f"Total Pengeluaran (Expense): {format_rupiah(totals['total_expense'])}")
    print(f"Saldo (Balance)            : {format_rupiah(totals['balance'])}")
    print("=" * 85 + "\n")

# Menampilkan daftar transaksi dalam format tabel
def show_list_transaction(transactions):
    if not transactions:
        print("No transactions available.")
        return

    # Header tabel
    headers = ['ID', 'Tanggal', 'Jenis', 'Kategori', 'Jumlah', 'Catatan']
    col_widths = [5, 12, 10, 15, 18, 25]  # Jumlah lebih lebar
    header_line = "".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    print(header_line)
    print("-" * sum(col_widths))

    def format_rupiah(amount):
        try:
            amt = float(amount)
        except Exception:
            return str(amount)
        return "Rp {:,.0f}".format(amt).replace(",", ".")

    # Isi tabel
    for t in transactions:
        print(f"{t.id:<5}{t.date:<12}{t.type:<10}{t.category:<15}{format_rupiah(t.amount):<18}{t.note:<25}")
    print("-" * sum(col_widths))
