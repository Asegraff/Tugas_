# Panduan Menjalankan di VSCode (Windows PowerShell)

## 📋 Persyaratan
- Python 3.9 atau lebih tinggi (sudah terinstall)
- VSCode
- Extension: "Python" dari Microsoft
- Windows PowerShell (built-in di Windows)

---

## 🎯 STEP-BY-STEP TUTORIAL

### **STEP 1: Buka Folder Project di VSCode**

1. Buka VSCode
2. Tekan `Ctrl+K Ctrl+O` atau klik File → Open Folder
3. Navigasi ke folder `Tugas_` dan klik "Select Folder"
4. Tunggu VSCode loading project

---

### **STEP 2: Buka Terminal PowerShell di VSCode**

**Cara 1 (Termudah):**
- Tekan `` Ctrl+` `` (backtick, di samping tombol 1)
- VSCode akan membuka terminal bawaan di bagian bawah

**Cara 2:**
- Klik menu View → Terminal
- atau klik "Terminal" di menu bar

**Cara 3:**
- Klik kanan di folder project → "Open in Integrated Terminal"

Hasil: Terminal akan terbuka di bawah VSCode, menunjukkan path folder

```
PS C:\Users\YourName\Tugas_>
```

---

### **STEP 3: Gunakan PowerShell untuk Setup Virtual Environment**

**A. Lihat Python terinstall (Opsional)**
```powershell
python --version
```

Hasilnya akan menunjukkan versi Python (contoh: `Python 3.11.5`)

**B. Buat Virtual Environment**
```powershell
python -m venv venv
```

⏳ Tunggu 1-2 menit sampai selesai. Jika tidak ada error, folder `venv` akan muncul di project.

**C. Activate Virtual Environment (PENTING!)**

Ketik perintah ini di PowerShell:
```powershell
venv\Scripts\Activate.ps1
```

✅ Jika berhasil, terminal akan menampilkan:
```
(venv) PS C:\Users\YourName\Tugas_>
```

Perhatikan tanda `(venv)` di depan - itu berarti virtual environment aktif.

**⚠️ Jika error: "cannot be loaded because running scripts is disabled"**

Jalankan command ini:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Tekan `Y` (Yes) saat ditanya. Kemudian jalankan lagi:
```powershell
venv\Scripts\Activate.ps1
```

---

### **STEP 4: Install Dependencies**

Pastikan `(venv)` terlihat di terminal. Kemudian ketik:
```powershell
pip install -r requirements.txt
```

⏳ Tunggu 2-3 menit. Ini akan install semua library yang dibutuhkan:
- openpyxl (Excel)
- pyodbc (Database Access)
- reportlab (PDF)
- pandas, dotenv, click, dll

Setelah selesai, Anda akan melihat:
```
Successfully installed openpyxl-3.10.8 pyodbc-4.0.39 ...
```

---

### **STEP 5: Select Python Interpreter di VSCode**

1. Tekan `Ctrl+Shift+P` untuk membuka Command Palette
2. Ketik: `Python: Select Interpreter`
3. Pilih yang menunjukkan `.\venv\Scripts\python.exe`

Sekarang VSCode tahu harus menggunakan Python dari virtual environment.

---

### **STEP 6: Setup Templates & Database**

Di PowerShell, ketik:
```powershell
python scripts/create_template.py
```

Akan muncul output:
```
==================================================
Sistem Invoice & Rekap ACU - Setup
==================================================
Creating Excel template...
✓ Excel template created: ./excel/Master_Dashboard.xlsm

Setting up database...
Note: Please ensure your Access database has the following tables:
  - MasterRig
  - MasterKategori
  - TransaksiHarian
  - Invoice
  - UserLogin
Database path: ./database/invoice_system.accdb

Creating default admin user...
✓ Admin user created (username: admin, password: admin123)
⚠ Please change the password after first login!

==================================================
Setup completed!
Run 'python main.py' to start the application
==================================================
```

---

### **STEP 7: JALANKAN APLIKASI** ✨

**Opsi A: Menggunakan Debug (Recommended)**

1. Tekan `F5` di keyboard
2. Aplikasi mulai berjalan di terminal VSCode
3. Anda akan melihat login prompt:

```
==================================================
LOGIN - Sistem Invoice & Rekap ACU
==================================================
Username: 
```

**Opsi B: Jalankan via PowerShell**

```powershell
python main.py
```

---

## 🎮 Login dan Menggunakan Aplikasi

Saat login prompt muncul, masukkan:
- **Username:** `admin`
- **Password:** `admin123`

Tekan Enter. Jika berhasil:

```
✓ Selamat datang admin!

==================================================
MENU UTAMA
==================================================
1. Input Transaksi Harian
2. View Transaksi
3. Generate Rekap
4. Manage Invoice
5. Backup & Restore
6. Logout
==================================================
Pilih menu (1-6): 
```

---

## 📝 Contoh Menggunakan Fitur

### **Contoh 1: Input Transaksi (Menu 1)**

```
Pilih menu (1-6): 1

==================================================
INPUT TRANSAKSI HARIAN
==================================================
Tanggal (YYYY-MM-DD): 2026-06-14

Daftar RIG:
1. 18 - RIG 18
2. 29 - RIG 29
3. 60 - RIG 60
... dst
Pilih RIG (nomor): 1

Daftar Kategori:
1. DSR - Daily Safety Report
2. VISITOR - Visitor
3. WSR - Weekly Safety Report
4. SERCO - Service Company
5. NDT - Non-Destructive Test
6. SEMBAKO - Sembako
Pilih Kategori (nomor): 1

Qty/Pax: 5
Harga: 100000

✓ Transaksi berhasil disimpan!
```

### **Contoh 2: View Transaksi (Menu 2)**

```
Pilih menu (1-6): 2

==================================================
VIEW TRANSAKSI
==================================================
Dari tanggal (YYYY-MM-DD): 2026-06-01
Sampai tanggal (YYYY-MM-DD): 2026-06-14

--------------------------------------------------------------------------------
Tanggal      RIG    Kategori   Qty    Harga           Total
--------------------------------------------------------------------------------
2026-06-14   18     DSR        5      100000          500000
2026-06-13   29     VISITOR    3      150000          450000
--------------------------------------------------------------------------------
```

### **Contoh 3: Generate Rekap (Menu 3)**

```
Pilih menu (1-6): 3

==================================================
GENERATE REKAP
==================================================
Dari tanggal (YYYY-MM-DD): 2026-06-01
Sampai tanggal (YYYY-MM-DD): 2026-06-14

----------------------------------------------------------------------
RIG    Kategori        Total Qty        Total Amount
----------------------------------------------------------------------
18     DSR             5                500000 IDR
18     VISITOR         2                300000 IDR
29     DSR             3                300000 IDR
29     VISITOR         1                150000 IDR
----------------------------------------------------------------------

✓ Rekap berhasil digenerate!
```

---

## 🔧 Konfigurasi Database Access

### **PENTING: Buat Database Sebelum Jalankan Aplikasi**

**Opsi 1: Gunakan File Template (Mudah)**
1. File database sudah ada di `database/invoice_system.accdb`
2. Tinggal buka di Microsoft Access dan tambah data

**Opsi 2: Buat Database Baru**

1. Buka Microsoft Access
2. Klik "Blank Database"
3. Beri nama: `invoice_system.accdb`
4. Save di folder: `database/` (di dalam project)
5. Buat tabel dengan struktur berikut:

#### **Tabel 1: MasterRig**
```
Nama Field      Tipe Data       Keterangan
-----------     -----------     ------------------
ID_Rig          Text            Primary Key
NamaRig         Text
Client          Text
```

#### **Tabel 2: MasterKategori**
```
Nama Field      Tipe Data       Keterangan
-----------     -----------     ------------------
ID_Kategori     Text            Primary Key
NamaKategori    Text
```

#### **Tabel 3: TransaksiHarian**
```
Nama Field      Tipe Data       Keterangan
-----------     -----------     ------------------
ID              AutoNumber      Primary Key
Tanggal         Date/Time
Rig             Text
Kategori        Text
Qty_Pax         Number (Long)
Harga           Currency
Total           Currency
```

#### **Tabel 4: Invoice**
```
Nama Field      Tipe Data       Keterangan
-----------     -----------     ------------------
ID_Invoice      AutoNumber      Primary Key
NoInvoice       Text
Rig             Text
Periode         Text            Format: YYYY-MM
NilaiInvoice    Currency
Status          Text
CreatedDate     Date/Time
UpdatedDate     Date/Time
```

#### **Tabel 5: UserLogin**
```
Nama Field      Tipe Data       Keterangan
-----------     -----------     ------------------
ID_User         AutoNumber      Primary Key
Username        Text            Unique
Password        Text
Role            Text            ADMIN/SUPERVISOR/OPERATOR
CreatedDate     Date/Time
UpdatedDate     Date/Time
```

6. Save dan tutup Microsoft Access
7. Jalankan aplikasi

---

## 🐛 Troubleshooting

### **Problem 1: "Python tidak dikenali"**

**Solusi:**
```powershell
# Cek versi Python
python --version

# Jika error, install Python dari:
# https://www.python.org/downloads/
# Saat install, CENTANG: "Add Python to PATH"
```

### **Problem 2: "cannot be loaded because running scripts is disabled"**

**Solusi:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Jawab: Y (Yes)
```

### **Problem 3: Virtual Environment tidak activate**

**Solusi:**
```powershell
# Pastikan di folder project yang benar
cd C:\Users\YourName\Tugas_

# Jalankan activate lagi
venv\Scripts\Activate.ps1

# Harus melihat (venv) di terminal
```

### **Problem 4: "ModuleNotFoundError: No module named 'pyodbc'"**

**Solusi:**
```powershell
# Pastikan sudah activate virtual environment
# Kemudian install ulang
pip install --upgrade pyodbc
```

### **Problem 5: "Database connection failed"**

**Solusi:**
1. Pastikan file `invoice_system.accdb` ada di folder `database/`
2. Pastikan database tidak sedang dibuka di Microsoft Access
3. Periksa konfigurasi di `.env` file
4. Buka file `.env` dan periksa path:
   ```
   DB_PATH=./database/invoice_system.accdb
   ```

### **Problem 6: "No such table: TransaksiHarian"**

**Solusi:**
Database belum memiliki tabel. Buat tabel sesuai panduan di atas di Microsoft Access.

---

## ✅ Checklist Sebelum Jalankan

- [ ] Python sudah terinstall (`python --version` bisa dijalankan)
- [ ] VSCode sudah terbuka dengan folder project
- [ ] Terminal PowerShell terbuka di VSCode (`` Ctrl+` ``)
- [ ] Virtual environment sudah dibuat (`venv` folder ada)
- [ ] Virtual environment sudah di-activate (`(venv)` terlihat di terminal)
- [ ] Dependencies sudah di-install (`pip install -r requirements.txt` selesai)
- [ ] Python interpreter di VSCode sudah set ke `.\venv\Scripts\python.exe`
- [ ] Database Access sudah dibuat dengan tabel yang benar
- [ ] Setup script sudah dijalankan (`python scripts/create_template.py`)
- [ ] File `Master_Dashboard.xlsm` sudah ada di folder `excel/`

---

## 🚀 Quick Reference

```powershell
# 1. Buka folder di VSCode: Ctrl+K Ctrl+O
# 2. Buka terminal: Ctrl+`
# 3. Buat venv: python -m venv venv
# 4. Activate venv: venv\Scripts\Activate.ps1
# 5. Install dependencies: pip install -r requirements.txt
# 6. Setup: python scripts/create_template.py
# 7. Run app: F5 (atau python main.py)
```

---

## 📞 Bantuan Lebih Lanjut

Jika masih ada masalah:
1. Lihat log di folder `logs/`
2. Cek pesan error di terminal
3. Pastikan semua langkah di checklist sudah selesai
4. Baca file `README.md` di project

**Selamat menggunakan Sistem Invoice & Rekap ACU! 🎉**
