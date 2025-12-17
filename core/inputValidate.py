from datetime import datetime
class inputValidate(Exception):
    def __call__(self):
        pass

    def date(self, prompt="Date (YYYY-MM-DD): "):
        while True:
            date_str = input(prompt)
            if date_str.lower() == "now":
                return datetime.now().strftime("%Y-%m-%d")
            try:
                datetime.strptime(date_str, "%Y-%m-%d")
                return date_str
            except ValueError:
                print("[X] Invalid date format! Use YYYY-MM-DD")

    def type(self, prompt="Type (Income/Expense): "):
        while True:
            t = input(prompt).capitalize()
            if t in ["I", "E"]:
                t = "Income" if t == "I" else "Expense"
            if t in ["Income", "Expense"]:
                return t
            print("[X] Type must be Income or Expense")

    def float(self, prompt="Amount: "):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("[X] Amount must be a number")

    def text(self, prompt="Input: "):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("[X] Input cannot be empty")
