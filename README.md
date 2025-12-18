# MaKu - Mahasiswa Keuangan
Maku adalah aplikasi manajemen keuangan yang dirancang khusus untuk mahasiswa universitas. Aplikasi ini membantu mahasiswa melacak pendapatan, pengeluaran, dan tabungan mereka untuk mengelola keuangan dengan lebih baik selama perjalanan akademis mereka. dibuat dengan Python dan Django Framework.

## Anggota Kelompok
- Nama: Aria Fatah Anom
  Nim : 0
- Nama: FAHRI MULYADI
  Nim : 0
- Nama: IZZUDIEN AL FAQIH
  Nim : 0
- Nama: RAFI AFRAND
  Nim : 0
- Nama: ZIKRA MAHKOTA HASAN
  Nim : 0

## how to setup
1. Clone repository ini ke lokal mesin Anda.
```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

2. Install dependencies yang diperlukan menggunakan pip.
```bash
pip3 install -r req.txt
```

3. running the app python
```bash
python3 maku.py cli
python3 maku.py web
```

4. ubah config (opsional)
- buka config.cfg, dan sesuaikan config
```INI
# Global configuration file
FILE_CSV = data/saku_data.csv
FILE_EXCEL = data/saku_data.xlsx
MODE = csv # Options: csv, excel

# Web server configuration
HOST = 0.0.0.0 # Server host
PORT = 8000 # Server port
```

<details>
<summary>How to setup django</summary>

```bash
python3 -m venv venv
.\venv\Scripts\activate

python -m django startproject web
cd web
pip3 install django
python3 manage.py runserver

# add app
python manage.py startapp transactions
```
</details>

<details>
<summary>How to Setup CPanel</summary>

1. go to terminal
```bash
cd /home/aria.my.id
git clone git clone https://github.com/ariafatah0711/Maku
cd Maku
```

2. add project python cpanel
![alt text](https://raw.githubusercontent.com/arialinux/image/refs/heads/main/image.png)

3. install package
```bash
source /home/ariamyid/virtualenv/aria.my.id/Maku/3.11/bin/activate && cd /home/ariamyid/aria.my.id/Maku
pip3 install -r req.txt
cat << EOF > /web/web/config/wsgi.py
<masukan kode wsgi nya>
EOF
```

4. restart aplikasi di cpanel

</details>

---

## Gak Kepake Ini
<details>
<summary>Nyoba pake API</summary>

```bash
## testing api
```bash
curl -X GET http://192.168.1.11:8000/api/transactions/
curl -X GET http://192.168.1.11:8000/api/transactions/ | jq
curl -X POST http://192.168.1.11:8000/api/transactions/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-12-18",
    "type": "income",
    "category": "salary",
    "amount": 5000,
    "note": "Gaji Desember"
  }'
curl -X PUT http://192.168.1.11:8000/api/transactions/3/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-12-19",
    "type": "expense",
    "category": "food",
    "amount": 150,
    "note": "Makan siang"
  }'
curl -X DELETE http://192.168.1.11:8000/api/transactions/3/
```

</details>
