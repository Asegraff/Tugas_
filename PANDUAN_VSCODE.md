# Panduan Menjalankan di VSCode

## 📋 Persyaratan
- Python 3.9 atau lebih tinggi
- VSCode
- Extension: "Python" dari Microsoft

## 📥 Instalasi Extension di VSCode

1. Buka VSCode
2. Tekan `Ctrl+Shift+X` (Windows/Linux) atau `Cmd+Shift+X` (Mac)
3. Cari "Python"
4. Klik "Install" pada extension "Python" dari Microsoft
5. Tunggu hingga selesai

## 🚀 Langkah-Langkah Menjalankan

### **Step 1: Clone Repository**

1. Buka Terminal di VSCode (`Ctrl+` atau View → Terminal)
2. Ketik perintah:
```bash
git clone https://github.com/Asegraff/Tugas_.git
cd Tugas_
git checkout feature/invoice-rekap-system
```

### **Step 2: Buat Virtual Environment**

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Untuk Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Setelah berhasil, terminal akan menampilkan `(venv)` di awal baris.

### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

Tunggu hingga semua library selesai terinstall.

### **Step 4: Select Python Interpreter**

1. Tekan `Ctrl+Shift+P` (Windows/Linux) atau `Cmd+Shift+P` (Mac)
2. Ketik: `Python: Select Interpreter`
3. Pilih yang berakhir dengan `./venv/bin/python` atau `./venv/Scripts/python.exe`

### **Step 5: Setup Database dan Templates**

1. Di Terminal VSCode, ketik:
```bash
python scripts/create_template.py
```

2. Ini akan membuat:
   - File Excel template: `excel/Master_Dashboard.xlsm`
   - Admin user di database
   - Folder-folder yang diperlukan

### **Step 6: Jalankan Aplikasi**

**Opsi A: Menggunakan Debug (Recommended)**

1. Tekan `F5` di keyboard
2. Pilih "Python: Run Main" dari dropdown yang muncul
3. Aplikasi akan mulai berjalan di terminal

**Opsi B: Menggunakan Terminal**

```bash
python main.py
```

## 🎮 Menggunakan Aplikasi

Setelah aplikasi berjalan, Anda akan melihat:

```
==================================================
LOGIN - Sistem Invoice & Rekap ACU
==================================================
Username: 
```

Masukkan credentials:
- **Username:** `admin`
- **Password:** `admin123`

Setelah login, Anda akan melihat MENU UTAMA dengan pilihan:
```
1. Input Transaksi Harian
2. View Transaksi
3. Generate Rekap
4. Manage Invoice
5. Backup & Restore
6. Logout
```

## 📝 Langkah-Langkah Detail untuk Setiap Menu

### **1. Input Transaksi Harian**
```
Pilih menu (1-6): 1
Tanggal (YYYY-MM-DD): 2026-06-14
Pilih RIG (nomor): 1
Pilih Kategori (nomor): 1
Qty/Pax: 10
Harga: 50000
→ ✓ Transaksi berhasil disimpan!
```

### **2. View Transaksi**
```
Pilih menu (1-6): 2
Dari tanggal (YYYY-MM-DD): 2026-06-01
Sampai tanggal (YYYY-MM-DD): 2026-06-30
→ Tampilan tabel transaksi
```

### **3. Generate Rekap**
```
Pilih menu (1-6): 3
Dari tanggal (YYYY-MM-DD): 2026-06-01
Sampai tanggal (YYYY-MM-DD): 2026-06-30
→ Summary per RIG dan Kategori
```

### **4. Manage Invoice**
```
Pilih menu (1-6): 4
1. Create Invoice
2. View Invoices
3. Update Status
4. Kembali
Pilih (1-4): 1
RIG: 18
Periode (YYYY-MM): 2026-06
Nilai Invoice: 500000
→ ✓ Invoice berhasil dibuat!
```

### **5. Backup & Restore**
```
Pilih menu (1-6): 5
1. Create Backup
2. View Backups
3. Restore Backup
4. Cleanup Old Backups
5. Kembali
Pilih (1-5): 1
Deskripsi backup: Backup rutin bulanan
→ ✓ Backup berhasil dibuat!
```

## 🔧 Setup Microsoft Access Database

### **Opsi 1: Menggunakan File Existing**
1. Pastikan file `.accdb` sudah ada di folder `database/`
2. Update path di `.env` jika perlu

### **Opsi 2: Membuat Database Baru di Microsoft Access**

1. Buka Microsoft Access
2. Create → Blank Database
3. Save sebagai `invoice_system.accdb` di folder `database/`
4. Buat table dengan struktur:

**MasterRig:**
```
ID_Rig (Text, Primary Key)
NamaRig (Text)
Client (Text)
```

**MasterKategori:**
```
ID_Kategori (Text, Primary Key)
NamaKategori (Text)
```

**TransaksiHarian:**
```
ID (AutoNumber, Primary Key)
Tanggal (Date/Time)
Rig (Text)
Kategori (Text)
Qty_Pax (Number)
Harga (Currency)
Total (Currency)
```

**Invoice:**
```
ID_Invoice (AutoNumber, Primary Key)
NoInvoice (Text)
Rig (Text)
Periode (Text)
NilaiInvoice (Currency)
Status (Text)
CreatedDate (Date/Time)
UpdatedDate (Date/Time)
```

**UserLogin:**
```
ID_User (AutoNumber, Primary Key)
Username (Text, Unique)
Password (Text)
Role (Text)
CreatedDate (Date/Time)
UpdatedDate (Date/Time)
```

## 🐛 Troubleshooting

### **Error: "No module named 'pyodbc'"**
```bash
pip install pyodbc
```

### **Error: "Python interpreter not found"**
1. Pastikan Python sudah terinstall
2. Buka Command Prompt dan ketik: `python --version`
3. Jika tidak recognized, install ulang Python dari python.org
4. Saat install, centang "Add Python to PATH"

### **Error: "Cannot connect to database"**
1. Pastikan file `.accdb` ada di path yang benar
2. Periksa konfigurasi di `.env`
3. Pastikan database tidak sedang dibuka di Microsoft Access

### **Error: "venv tidak ditemukan"**
```bash
python -m venv venv
```
Jalankan command di atas lagi

### **Error: "Terminal says command not found"**
Pastikan sudah activate virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

## 📂 File yang Penting

```
.env                          → Konfigurasi sistem (copy dari .env.example)
main.py                       → File utama, jalankan ini
database/
  └─ invoice_system.accdb    → Database Access (buat sendiri atau gunakan existing)
excel/
  └─ Master_Dashboard.xlsm   → Auto-created saat setup
config/
  └─ settings.py            → Baca dari .env
```

## 💡 Tips

1. **Jika ingin menjalankan ulang**, cukup tekan `F5` lagi atau jalankan `python main.py`
2. **Untuk stop aplikasi**, tekan `Ctrl+C` di terminal
3. **Gunakan `Ctrl+` untuk buka/tutup terminal di VSCode**
4. **Jika ada error, lihat message di terminal untuk clue**
5. **Log files tersimpan di folder `logs/` untuk referensi**

## ✅ Verifikasi Instalasi

Jika semua berjalan dengan baik, Anda akan melihat:

```
==================================================
Sistem Invoice & Rekap ACU
==================================================
INFO:root:Database connected: ./database/invoice_system.accdb
INFO:root:User admin authenticated successfully

LOGIN - Sistem Invoice & Rekap ACU
==================================================
Username: admin
Password: ****
✓ Selamat datang admin!
```

---

**Sudah siap? Mulai gunakan aplikasi! 🚀**

Jika ada pertanyaan, cek file `.env` atau logs di folder `logs/`.
