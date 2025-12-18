import sys, os
import pandas as pd

# add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.models import Transaction
from core.util import check_file
from utils import ReadConfig, show_list_transaction

FIELD_NAMES = ['id', 'tanggal', 'jenis', 'kategori', 'jumlah', 'catatan']

def _ensure_excel(path):
    if not os.path.exists(path):
        pd.DataFrame(columns=FIELD_NAMES).to_excel(path, index=False)

class ExcelHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        check_file(file_path)
        _ensure_excel(file_path)

    def _load_df(self):
        return pd.read_excel(self.file_path)

    def _save_df(self, df):
        df.to_excel(self.file_path, index=False)

    def read(self):
        return [
            Transaction(
                id=row.id,
                date=row.tanggal,
                type=row.jenis,
                category=row.kategori,
                amount=(row.jumlah or 0),
                note=row.catatan or ''
            )
            for row in self._load_df().itertuples()
        ]

    def write(self, tx: Transaction):
        df = self._load_df()
        df.loc[len(df)] = [
            tx.id, tx.date, tx.type,
            tx.category, tx.amount, tx.note
        ]
        self._save_df(df)

    def delete(self, id):
        df = self._load_df()
        df = df[df.id.astype(str) != str(id)].reset_index(drop=True)
        df['id'] = range(1, len(df) + 1)
        self._save_df(df)

    def update(self, tx: Transaction):
        df = self._load_df()
        df.loc[df.id.astype(str) == str(tx.id),
               ['tanggal', 'jenis', 'kategori', 'jumlah', 'catatan']] = \
            [tx.date, tx.type, tx.category, tx.amount, tx.note]
        self._save_df(df)

# ======= Test Code =======
if __name__ == "__main__":
    excel = ExcelHandler(ReadConfig('FILE_EXCEL'))

    print("[+] Before Write")
    show_list_transaction(excel.read())

    excel.write(Transaction(999, '2024-01-01', 'income', 'salary', 5000, 'January salary'))

    print("\n[+] Write Data Excel - ID 999")
    show_list_transaction(excel.read())

    excel.delete(999)
    excel.update(Transaction(1, '2024-02-02', 'expense', 'groceries', 150, 'February groceries'))
    print("\n[+] After Delete - ID 999 And Update - ID 1")
    show_list_transaction(excel.read())
