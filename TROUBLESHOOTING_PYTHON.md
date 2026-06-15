# Troubleshooting: Python Tidak Bisa Terinstall

## 🔍 Diagnosa Masalah

### **Step 1: Cek Apakah Python Sudah Terinstall**

1. Buka **PowerShell** (tekan `Win+R`, ketik `powershell`, Enter)
2. Ketik command:
   ```powershell
   python --version
   ```
3. Lihat hasilnya:
   - ✅ **Jika muncul versi**: Python sudah terinstall
   - ❌ **Jika error "python is not recognized"**: Python belum terinstall

---

## ❌ SOLUSI 1: Python Belum Terinstall

### **Download Python**

1. Buka browser, ke: **https://www.python.org/downloads/**
2. Klik tombol kuning **"Download Python 3.11.5"** (atau versi terbaru)
3. File `python-3.11.5-amd64.exe` akan didownload

### **Install Python**

1. Double-click file `python-3.11.5-amd64.exe`
2. **PENTING: Centang kotak "Add python.exe to PATH"**
   
   ```
   ☑ Add Python 3.11 to PATH  ← CENTANG INI!
   ```

3. Klik **"Install Now"** atau **"Customize Installation"** (Next, Next, Finish)
4. Tunggu instalasi selesai
5. Tutup installer

### **Verifikasi Instalasi**

1. Buka **PowerShell** baru
2. Ketik:
   ```powershell
   python --version
   ```
3. Harus muncul:
   ```
   Python 3.11.5
   ```

Jika sudah muncul, Python berhasil terinstall! ✅

---

## ❌ SOLUSI 2: Python Terinstall tapi "Not Recognized"

Artinya: Python terinstall tapi PATH tidak terdaftar di Windows.

### **Cara 1: Reinstall Python (Termudah)**

1. Uninstall Python:
   - Buka Control Panel → Programs → Programs and Features
   - Cari "Python 3.x.x"
   - Klik kanan → Uninstall

2. Install ulang Python **DENGAN CENTANG "Add to PATH"**
   - Download dari: https://www.python.org/downloads/
   - Saat install, pastikan ☑ **"Add python.exe to PATH"**
   - Klik "Install Now"

3. Buka PowerShell baru dan cek:
   ```powershell
   python --version
   ```

### **Cara 2: Tambah PATH Manual (Advanced)**

**Jika tidak mau reinstall:**

1. Cari di mana Python diinstall:
   - Biasanya di: `C:\Users\YourName\AppData\Local\Programs\Python\Python311`
   - Atau: `C:\Program Files\Python311`

2. Edit Environment Variables:
   - Tekan `Win+R`, ketik: `sysdm.cpl`
   - Klik tab **"Advanced"**
   - Klik button **"Environment Variables"**
   - Di bagian "System variables", cari "Path"
   - Klik "Edit"
   - Klik "New"
   - Paste path Python (contoh: `C:\Users\YourName\AppData\Local\Programs\Python\Python311`)
   - Klik OK, OK, OK

3. Tutup PowerShell, buka PowerShell **baru**
   ```powershell
   python --version
   ```

---

## ❌ SOLUSI 3: Python Versi Salah

Python harus versi **3.9 atau lebih tinggi**.

### **Cek Versi**
```powershell
python --version
```

**Jika versi < 3.9** (contoh: 3.7, 3.8):
- Download versi terbaru: https://www.python.org/downloads/
- Uninstall versi lama
- Install versi baru

---

## ✅ SOLUSI 4: Gunakan `python3` bukannya `python`

Sebagian Windows menggunakan `python3` bukan `python`.

### **Coba di PowerShell:**
```powershell
python3 --version
```

Jika ini yang berhasil, gunakan `python3` di semua command:
```powershell
python3 -m venv venv
python3 -m pip install -r requirements.txt
python3 main.py
```

---

## ❌ SOLUSI 5: PIP Tidak Terinstall

Python sudah ada tapi `pip` (package installer) tidak ada.

### **Install PIP**

```powershell
python -m ensurepip --upgrade
```

Jika error, coba:
```powershell
python -m pip install --upgrade pip
```

---

## ✅ SOLUSI 6: Virtual Environment Error

Jika Python terinstall tapi error saat buat `venv`:

### **Error: "No module named 'venv'"**

Solusi:
```powershell
python -m pip install virtualenv
virtualenv venv
venv\Scripts\Activate.ps1
```

---

## 📋 CHECKLIST Instalasi Python yang Benar

Setelah install Python, pastikan:

- [ ] Buka PowerShell **BARU** (penting!)
- [ ] Jalankan: `python --version` → muncul versi
- [ ] Jalankan: `python -m pip --version` → muncul versi pip
- [ ] Jalankan: `python -m venv test_venv` → folder test_venv muncul
- [ ] Jalankan: `test_venv\Scripts\Activate.ps1` → `(test_venv)` muncul
- [ ] Bersihkan: `rmdir /s test_venv` → hapus folder test

Jika semua berhasil ✅, Python siap digunakan!

---

## 🚀 Setelah Python Terinstall: Langkah Berikutnya

```powershell
# 1. Buka folder project di VSCode
cd C:\path\to\Tugas_

# 2. Buka terminal di VSCode (Ctrl+`)

# 3. Buat virtual environment
python -m venv venv

# 4. Activate
venv\Scripts\Activate.ps1

# 5. Install dependencies
pip install -r requirements.txt

# 6. Setup
python scripts/create_template.py

# 7. Run
python main.py
```

---

## 💬 Jika Masih Error

Jika sudah ikuti semua solusi tapi masih error, beri tahu:

1. **Output error yang muncul** (copy-paste di GitHub issue)
2. **Hasil dari**:
   ```powershell
   python --version
   python -m pip --version
   where python
   ```
3. **Windows version Anda** (cek: Settings → System → About)

---

**Jangan khawatir, Python pasti bisa terinstall! Ikuti langkah-langkah di atas. 🎯**
