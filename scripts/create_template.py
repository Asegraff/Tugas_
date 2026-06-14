#!/usr/bin/env python
"""Create Excel template and initialize database"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from excel import ExcelWorkbook
from config.settings import settings
from utils.logger import setup_logger

logger = setup_logger('create_template')

def create_excel_template():
    """Create master Excel workbook"""
    print("Creating Excel template...")
    excel = ExcelWorkbook()
    if excel.create_master_workbook():
        print(f"✓ Excel template created: {settings.EXCEL_TEMPLATE_PATH}")
    else:
        print("✗ Failed to create Excel template")

def setup_database():
    """Setup database schema"""
    print("\nSetting up database...")
    print("Note: Please ensure your Access database has the following tables:")
    print("  - MasterRig")
    print("  - MasterKategori")
    print("  - TransaksiHarian")
    print("  - Invoice")
    print("  - UserLogin")
    print(f"Database path: {settings.DB_PATH}")

def create_admin_user():
    """Create default admin user"""
    print("\nCreating default admin user...")
    from modules import UserManager
    
    user_mgr = UserManager()
    if user_mgr.create_user('admin', 'admin123', 'ADMIN'):
        print("✓ Admin user created (username: admin, password: admin123)")
        print("⚠ Please change the password after first login!")
    else:
        print("✗ Failed to create admin user (may already exist)")

if __name__ == '__main__':
    print("="*50)
    print("Sistem Invoice & Rekap ACU - Setup")
    print("="*50)
    
    create_excel_template()
    setup_database()
    create_admin_user()
    
    print("\n" + "="*50)
    print("Setup completed!")
    print("Run 'python main.py' to start the application")
    print("="*50)
