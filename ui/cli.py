"""Command Line Interface for Invoice System"""

import logging
from typing import Optional
from modules import TransactionManager, InvoiceManager, UserManager, BackupManager
from utils.formatters import format_currency, format_date
from config.constants import RIGS, CATEGORIES
from datetime import datetime

logger = logging.getLogger(__name__)

class CLI:
    """Command Line Interface"""
    
    def __init__(self):
        self.transaction_mgr = TransactionManager()
        self.invoice_mgr = InvoiceManager()
        self.user_mgr = UserManager()
        self.backup_mgr = BackupManager()
        self.current_user = None
    
    def run(self):
        """Run CLI application"""
        self.show_login_menu()
        
        if self.current_user:
            self.show_main_menu()
    
    def show_login_menu(self):
        """Display login menu"""
        print("\n" + "="*50)
        print("LOGIN - Sistem Invoice & Rekap ACU")
        print("="*50)
        
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        user = self.user_mgr.authenticate(username, password)
        if user:
            self.current_user = user
            print(f"\n✓ Selamat datang {username}!")
        else:
            print("\n✗ Username atau password salah!")
    
    def show_main_menu(self):
        """Display main menu"""
        while True:
            print("\n" + "="*50)
            print("MENU UTAMA")
            print("="*50)
            print("1. Input Transaksi Harian")
            print("2. View Transaksi")
            print("3. Generate Rekap")
            print("4. Manage Invoice")
            print("5. Backup & Restore")
            print("6. Logout")
            print("="*50)
            
            choice = input("Pilih menu (1-6): ").strip()
            
            if choice == '1':
                self.menu_input_transaction()
            elif choice == '2':
                self.menu_view_transactions()
            elif choice == '3':
                self.menu_generate_recap()
            elif choice == '4':
                self.menu_manage_invoice()
            elif choice == '5':
                self.menu_backup()
            elif choice == '6':
                print("\nLogout berhasil. Terima kasih!")
                break
            else:
                print("\n✗ Pilihan tidak valid!")
    
    def menu_input_transaction(self):
        """Input transaction menu"""
        print("\n" + "="*50)
        print("INPUT TRANSAKSI HARIAN")
        print("="*50)
        
        tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
        
        print("\nDaftar RIG:")
        for i, rig in enumerate(list(RIGS.keys()), 1):
            print(f"{i}. {rig} - {RIGS[rig]['name']}")
        rig_choice = int(input("Pilih RIG (nomor): ")) - 1
        rig = list(RIGS.keys())[rig_choice]
        
        print("\nDaftar Kategori:")
        for i, (cat_key, cat) in enumerate(CATEGORIES.items(), 1):
            print(f"{i}. {cat['code']} - {cat['name']}")
        cat_choice = int(input("Pilih Kategori (nomor): ")) - 1
        kategori = list(CATEGORIES.keys())[cat_choice]
        
        qty_pax = int(input("Qty/Pax: "))
        harga = float(input("Harga: "))
        
        if self.transaction_mgr.add_transaction(tanggal, rig, kategori, qty_pax, harga):
            print("\n✓ Transaksi berhasil disimpan!")
        else:
            print("\n✗ Gagal menyimpan transaksi!")
    
    def menu_view_transactions(self):
        """View transactions menu"""
        print("\n" + "="*50)
        print("VIEW TRANSAKSI")
        print("="*50)
        
        start_date = input("Dari tanggal (YYYY-MM-DD): ").strip()
        end_date = input("Sampai tanggal (YYYY-MM-DD): ").strip()
        
        transactions = self.transaction_mgr.get_transactions_by_period(start_date, end_date)
        
        if transactions:
            print("\n" + "-"*80)
            print(f"{'Tanggal':<12} {'RIG':<6} {'Kategori':<10} {'Qty':<6} {'Harga':<15} {'Total':<15}")
            print("-"*80)
            for txn in transactions:
                print(f"{txn['Tanggal']:<12} {txn['Rig']:<6} {txn['Kategori']:<10} {txn['Qty_Pax']:<6} {txn['Harga']:<15} {txn['Total']:<15}")
            print("-"*80)
        else:
            print("\n✗ Tidak ada transaksi ditemukan")
    
    def menu_generate_recap(self):
        """Generate recap menu"""
        print("\n" + "="*50)
        print("GENERATE REKAP")
        print("="*50)
        
        start_date = input("Dari tanggal (YYYY-MM-DD): ").strip()
        end_date = input("Sampai tanggal (YYYY-MM-DD): ").strip()
        
        summary = self.transaction_mgr.get_summary_by_period(start_date, end_date)
        
        if summary:
            print("\n" + "-"*70)
            print(f"{'RIG':<6} {'Kategori':<15} {'Total Qty':<15} {'Total Amount':<20}")
            print("-"*70)
            for row in summary:
                print(f"{row['Rig']:<6} {row['Kategori']:<15} {row['Total_Qty']:<15} {format_currency(row['Total_Amount'])}")
            print("-"*70)
            print("\n✓ Rekap berhasil digenerate!")
        else:
            print("\n✗ Tidak ada data untuk direkap")
    
    def menu_manage_invoice(self):
        """Manage invoice menu"""
        print("\n" + "="*50)
        print("MANAGE INVOICE")
        print("="*50)
        print("1. Create Invoice")
        print("2. View Invoices")
        print("3. Update Status")
        print("4. Kembali")
        print("="*50)
        
        choice = input("Pilih (1-4): ").strip()
        
        if choice == '1':
            self.create_invoice_menu()
        elif choice == '2':
            self.view_invoices_menu()
        elif choice == '3':
            self.update_invoice_status_menu()
    
    def create_invoice_menu(self):
        """Create invoice submenu"""
        rig = input("RIG: ").strip()
        periode = input("Periode (YYYY-MM): ").strip()
        nilai = float(input("Nilai Invoice: "))
        
        if self.invoice_mgr.create_invoice(rig, periode, nilai):
            print("\n✓ Invoice berhasil dibuat!")
        else:
            print("\n✗ Gagal membuat invoice!")
    
    def view_invoices_menu(self):
        """View invoices submenu"""
        periode = input("Periode (YYYY-MM): ").strip()
        invoices = self.invoice_mgr.get_invoices_by_period(periode)
        
        if invoices:
            print("\n" + "-"*80)
            print(f"{'No Invoice':<20} {'RIG':<6} {'Nilai':<20} {'Status':<15}")
            print("-"*80)
            for inv in invoices:
                print(f"{inv['NoInvoice']:<20} {inv['Rig']:<6} {format_currency(inv['NilaiInvoice']):<20} {inv['Status']:<15}")
            print("-"*80)
        else:
            print("\n✗ Tidak ada invoice ditemukan")
    
    def update_invoice_status_menu(self):
        """Update invoice status submenu"""
        invoice_id = int(input("Invoice ID: "))
        status = input("Status baru (DRAFT/PENDING/APPROVED/SENT/PAID): ").strip().upper()
        
        if self.invoice_mgr.update_invoice_status(invoice_id, status):
            print("\n✓ Status invoice berhasil diupdate!")
        else:
            print("\n✗ Gagal mengupdate status invoice!")
    
    def menu_backup(self):
        """Backup menu"""
        print("\n" + "="*50)
        print("BACKUP & RESTORE")
        print("="*50)
        print("1. Create Backup")
        print("2. View Backups")
        print("3. Restore Backup")
        print("4. Cleanup Old Backups")
        print("5. Kembali")
        print("="*50)
        
        choice = input("Pilih (1-5): ").strip()
        
        if choice == '1':
            description = input("Deskripsi backup: ").strip()
            if self.backup_mgr.create_backup(description):
                print("\n✓ Backup berhasil dibuat!")
            else:
                print("\n✗ Gagal membuat backup!")
        elif choice == '2':
            backups = self.backup_mgr.get_backups()
            if backups:
                print("\nDaftar Backup:")
                for i, backup in enumerate(backups, 1):
                    print(f"{i}. {backup.name}")
            else:
                print("\n✗ Tidak ada backup ditemukan")
        elif choice == '3':
            print("\n⚠ Fitur restore dalam pengembangan")
        elif choice == '4':
            if self.backup_mgr.cleanup_old_backups():
                print("\n✓ Old backups berhasil dihapus!")
            else:
                print("\n✗ Gagal menghapus old backups!")
