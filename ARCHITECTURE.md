# MaKu — Architecture & Flow
This document summarizes the project layout, component responsibilities, and the main runtime flows (Web and CLI) to make the codebase easier to read and modify.

## MaKu — Arsitektur & Alur Aplikasi
Dokumen ini menjelaskan struktur proyek, tanggung jawab tiap komponen, serta alur utama (Web dan CLI) supaya lebih mudah dibaca dan dikembangkan.

### Ringkasan Tingkat Tinggi
- Tujuan: Aplikasi pencatat keuangan pribadi dengan antarmuka CLI dan Web.
- Titik masuk utama:
  - `maku.py` — launcher utama untuk CLI dan untuk menjalankan server Web.
  - `web/manage.py` — utilitas Django (dipanggil saat mode `web`).

### Struktur Proyek (folder & file penting)
- `maku.py` — entry point, memilih mode CLI atau Web.
- `config.cfg` — konfigurasi sederhana (FILE_EXCEL, EXPORT_DIR, HOST, PORT).
- `core/` — logika bisnis dan akses data
  - `core/readConfig.py` — membaca `config.cfg`.
  - `core/logic.py` — logika transaksi (filter, agregasi, total).
  - `core/handlers/` — pembaca/penulis CSV & Excel.
- `cli/` — helper UI CLI (`display.py`, `inputValidate.py`).
- `web/` — aplikasi Django
  - `web/manage.py` — perintah Django
  - `web/views.py` — view-level helper (`_site_context()` berisi `REPO_URL` dll.)
  - `web/config/settings.py` — pengaturan Django
  - `web/app/` — app Django untuk fitur transaksi (template & views)
  - `web/templates/` — template Django (`base.html`, `home.html`, `contact.html`, `gallery.html`, `component/navbar.html`)
  - `web/static/` — aset statis (CSS, gambar)

### Tree proyek (ringkas — hanya file/folder penting)
```bash
Maku/
│
├── maku.py
├── config.cfg
├── requirements.txt
│
├── core/
│   ├── logic.py
│   ├── models.py
│   ├── read_config.py
│   ├── utils.py
│   └── handlers/
│       ├── csv_handler.py
│       └── excel_handler.py
│
├── cli/
│   ├── display.py
│   └── input_validate.py
│
├── web/
│   ├── manage.py
│   ├── urls.py
│   ├── views.py
│   │
│   ├── app/
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/
│   │       ├── app.html
│   │       └── edit.html
│   │
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── contact.html
│   │   └── gallery.html
│   │
│   └── static/
│       ├── css/
│       └── images/
│
├── _data/
│   └── saku_data.xlsx
└── _exports/
    └── 2026-01-11_101608.xlsx
```

### Alur Web singkat (Bahasa Indonesia)
1. Jalankan server web:
   ```bash
   python3 maku.py web
   ```
2. Django menerima request → `web/urls.py` → view (`web/views.py` atau `web/app/views.py`).
3. View mengumpulkan konteks (variabel situs seperti `REPO_URL` disediakan oleh `_site_context()` di `web/views.py`) lalu merender template.
4. Template menggunakan aset di `web/static/` dan menampilkan data yang disediakan oleh `core/`.

### Alur CLI singkat (Bahasa Indonesia)
1. Jalankan CLI:
   ```bash
   python3 maku.py cli
   ```
2. Menu CLI di `maku.py` menampilkan opsi, memanggil helper di `cli/` dan menggunakan `core/` untuk operasi data.

### Di mana ubah konfigurasi & variabel situs
- File `config.cfg` untuk konfigurasi runtime (FILE_EXCEL, EXPORT_DIR, HOST, PORT).
- Untuk label situs (REPO / LIVE_DEMO) edit fungsi `_site_context()` di `web/views.py`.
