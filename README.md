# Sistem Invoice & Rekap ACU

Sistem terintegrasi untuk manajemen invoice dan rekap transaksi harian dengan database Access dan Excel.

## Fitur Utama
- Input Transaksi Harian
- Generate Rekap Otomatis
- Generate Invoice
- Export PDF
- Dashboard Monitoring
- Login & User Management
- Backup Otomatis

## Requirements
- Python 3.9+
- VSCode
- Microsoft Access Database (ACCDB)
- openpyxl
- pyodbc
- reportlab (untuk PDF)

## Instalasi

```bash
pip install -r requirements.txt
```

## Struktur Folder
```
.
├── config/              # Konfigurasi sistem
├── database/            # Database schemas & queries
├── modules/             # Module utama
├── ui/                  # Interface
├── utils/               # Utility functions
├── excel/               # Template Excel
├── backup/              # Backup files
└── logs/                # Log files
```

## Running

```bash
python main.py
```
