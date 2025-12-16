import os

class Color:
    RED = "#FF0000"
    GREEN = "#00FF00"
    BLUE = "#0000FF"
    YELLOW = "#FFFF00"
    BLACK = "#000000"
    WHITE = "#FFFFFF"
    GRAY = "#808080"
    ORANGE = "#FFA500"

# Configuration reading utility
def ReadConfig(key = None):
    import configparser
    config = configparser.ConfigParser()

    # Get the project root (parent of 'core' directory)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root, 'config.cfg')

    config.read_string('[DEFAULT]\n' + open(config_path).read())
    if key == None:
        return config['DEFAULT']
    return config['DEFAULT'].get(key)

def ReadAllConfig():
    return {
        'FILE_CSV': ReadConfig('FILE_CSV'),
        'FILE_EXCEL': ReadConfig('FILE_EXCEL'),
        'MODE': ReadConfig('MODE')
    }

# Additional utility functions
def transaction_to_dict(t):
    return {
        'id': t.id,
        'tanggal': t.date,
        'jenis': t.type,
        'kategori': t.category,
        'jumlah': t.amount,
        'catatan': t.note
    }

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
