import sys, time, subprocess

# add project root
from core import *
from utils import *

CONFIG = ReadAllConfig()

MODE = str(CONFIG["MODE"])
EXPORT_DIR = str(CONFIG.get("EXPORT_DIR", "exports"))
HOST = CONFIG.get("HOST", "127.0.0.1")
PORT = CONFIG.get("PORT", "8000")

file_path = CONFIG["FILE_CSV"] if MODE == 'csv' else CONFIG["FILE_EXCEL"]

data = TransactionLogic(file_path, MODE)

def run_web():
    show_header("Maku - Mahasiswa Keuangan (Web Mode)")
    print(f"[i] Mode: {MODE.upper()} | File: {file_path}")
    print("[i] Starting Django web server...")
    try:
        subprocess.run([sys.executable, "web/manage.py", "runserver", f"{HOST}:{PORT}"]
                       )
    except KeyboardInterrupt:
        print("\n[!] Stopping web server...")
        time.sleep(0.5)
    except Exception as e:
        print(f"[X] An error occurred while starting the web server: \n{e}")
        time.sleep(0.5)

def run_cli():
    try:
        while True:
            show_header("Maku - Mahasiswa Keuangan (CLI Mode)")
            print(f"[i] Mode: {MODE.upper()} | File: {file_path}\n")
            show_main_menu()
            time.sleep(0.2)
            user = input("\n[?] Select an option (q/x to exit) \t\t: ")

            try:
                if user == 1 or user == '1':
                    # List Transactions
                    transactions = data.list_transactions()
                    show_header("List of Transactions")
                    show_list_transaction(transactions)
                    input("\n[O] Press Enter to return to the main menu... ")
                    time.sleep(0.3)

                elif user == 2 or user == '2':
                    # Add Transaction
                    ErrorText = inputValidate()
                    while True:
                        date = ErrorText.date("[?] Date (YYYY-MM-DD) (or 'now') \t\t: ")
                        type = ErrorText.type("[?] Type (Income/Expense) (or 'I' / 'E') \t: ")
                        category = input("[?] Category (Optional) \t\t\t: ")
                        amount = ErrorText.float("[?] Amount \t\t\t\t\t: ")
                        note = input("[?] Note (Optional) \t\t\t\t: ")
                        transaction = data.add_transaction(date, type, category, amount, note)
                        print("\n[✔] Transaction added successfully")
                        time.sleep(1)
                        break

                elif user == 3 or user == '3':
                    # Edit Transaction
                    transactions = data.list_transactions()
                    show_header("List of Transactions")
                    show_list_transaction(transactions)
                    edit_id = input("[?] Enter Transaction ID to edit: ")
                    ErrorText = inputValidate()
                    try:
                        date = ErrorText.date("[?] New Date (YYYY-MM-DD or now) (or leave blank): ", allow_blank=True)
                        type = ErrorText.type("[?] New Type (I / E) (or leave blank): ", allow_blank=True)
                        category = input("[?] New Category (or leave blank): ")
                        amount = ErrorText.float("[?] New Amount (or leave blank): ", allow_blank=True)
                        note = input("[?] New Note (or leave blank): ")
                        # Only pass non-blank values
                        kwargs = {}
                        if date: kwargs['date'] = date
                        if type: kwargs['type'] = type
                        if category: kwargs['category'] = category
                        if amount != '' and amount is not None: kwargs['amount'] = amount
                        if note: kwargs['note'] = note
                        data.edit_transaction(edit_id, **kwargs)
                        print("\n[✔] Transaction updated successfully")
                        time.sleep(1)
                    except Exception as e:
                        print(f"[X] Failed to update: {e}")
                        time.sleep(1)

                elif user == 4 or user == '4':
                    # Delete Transaction
                    transactions = data.list_transactions()
                    show_header("List of Transactions")
                    show_list_transaction(transactions)
                    del_id = input("[?] Enter Transaction ID to delete: ")
                    try:
                        data.delete_transaction(del_id)
                        print("\n[✔] Transaction deleted successfully")
                        time.sleep(1)
                    except Exception as e:
                        print(f"[X] Failed to delete: {e}")
                        time.sleep(1)

                elif user == 5 or user == '5':
                    # Export Transactions (automatic Excel export under ./export/)
                    try:
                        export_path = data.export_transactions(EXPORT_DIR)
                        print(f"\n[✔] Transactions exported successfully to {export_path}")
                        input("[O] Press Enter to return to the main menu... ")
                        time.sleep(0.5)
                    except Exception as e:
                        print(f"[X] Failed to export: {e}")
                        time.sleep(1)

                elif user in ['q', 'x']:
                    print("[!] Exiting...")
                    time.sleep(0.5)
                    break

                else:
                    print("[X] Invalid option!")
                    time.sleep(0.5)
            except KeyboardInterrupt:
                print("\n[!] Operation cancelled, returning to main menu...")
                time.sleep(1)
                continue

    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        time.sleep(0.5)
    except Exception as e:
        print(f"[X] An error occurred: \n{e}")
        time.sleep(0.5)

if __name__ == "__main__":
    print("[i] Welcome to Maku - Mahasiswa Keuangan")
    argument = sys.argv[1] if len(sys.argv) > 1 else ""

    if argument == "web":
        run_web()
    elif argument == "cli":
        run_cli()
    else:
        print("[X] Please specify the MODE to run the application: 'cli' or 'web'.")
