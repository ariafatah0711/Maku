import sys, os, time

# add project root
from core import *
from storage.csv_handler import CSVHandler

CONFIG = ReadAllConfig()

if __name__ == "__main__":
    try:
        csv_data = CSVHandler(CONFIG["FILE_CSV"])

        while True:
            show_header("Transaction Manager")
            show_main_menu()

            transactions = csv_data.read()
            time.sleep(0.2)
            user = input("\n[?] Select an option (q/x to exit) \t\t: ")

            # List Transactions
            if user == 1 or user == '1':
                time.sleep(0.3)
                show_header("List of Transactions")
                show_list_transaction(transactions)
                input("\n[O] Press Enter to return to the main menu...")

            # Add Transaction
            elif user == 2 or user == '2':
                transactions = csv_data.read()
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
                        csv_data.write(transaction)

                        print("\n[✔] Transaction added successfully")
                        time.sleep(1)
                        break
                except KeyboardInterrupt:
                    # User pressed Ctrl+C while entering fields — cancel add and return
                    print("\n[!] Add cancelled, returning to main menu...")
                    time.sleep(1)
                    continue

            # Update Transaction
            elif user == 3 or user == '3':
                pass

            # Delete Transaction
            elif user == 4 or user == '4':
                time.sleep(0.3)
                show_header("List of Transactions")
                show_list_transaction(transactions)
                del_id = input("[?] Enter Transaction ID to delete: ")
                csv_data.delete(del_id)
                print("\n[✔] Transaction deleted successfully")
                time.sleep(1)

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
