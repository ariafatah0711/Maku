import sys, os, time

# add project root
from core import *

CONFIG = ReadAllConfig()

if __name__ == "__main__":
    try:
        mode = str(CONFIG["MODE"])
        file_path = CONFIG["FILE_CSV"] if mode == 'csv' else CONFIG["FILE_EXCEL"]

        data = TransactionLogic(file_path, mode)

        while True:
            show_header("Transaction Manager")
            print(f"[i] Mode: {mode.upper()} | File: {file_path}\n")
            show_main_menu()

            time.sleep(0.2)
            user = input("\n[?] Select an option (q/x to exit) \t\t: ")

            # List Transactions
            if user == 1 or user == '1':
                data.list_transactions()

            # Add Transaction
            elif user == 2 or user == '2':
                data.add_transaction()

            # Update Transaction
            elif user == 3 or user == '3':
                pass

            # Delete Transaction
            elif user == 4 or user == '4':
                data.delete_transaction()

            elif user in ['q', 'x']:
                print("[!] Exiting...")
                time.sleep(0.5)
                break

            else:
                print("[X] Invalid option!")
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        time.sleep(0.5)
    except Exception as e:
        print(f"[X] An error occurred: \n{e}")
        time.sleep(0.5)
