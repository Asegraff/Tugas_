"""Application Settings"""

import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Settings:
    """Centralized settings management"""
    
    # Base paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # Database
    DB_PATH = os.getenv('DB_PATH', str(BASE_DIR / 'database' / 'invoice_system.accdb'))
    DB_DRIVER = os.getenv('DB_DRIVER', 'Microsoft Access Driver (*.mdb, *.accdb)')
    
    # Excel
    EXCEL_TEMPLATE_PATH = os.getenv('EXCEL_TEMPLATE_PATH', str(BASE_DIR / 'excel' / 'Master_Dashboard.xlsm'))
    
    # Paths
    PDF_OUTPUT_PATH = BASE_DIR / os.getenv('PDF_OUTPUT_PATH', 'output/pdf')
    BACKUP_PATH = BASE_DIR / os.getenv('BACKUP_PATH', 'backup')
    LOG_PATH = BASE_DIR / 'logs'
    
    # Data
    RIGS = os.getenv('RIGS', '18,29,60,61,82,87,89,90,92,94').split(',')
    
    # Backup
    BACKUP_INTERVAL = int(os.getenv('BACKUP_INTERVAL', '7'))
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Create required directories
    PDF_OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
    BACKUP_PATH.mkdir(parents=True, exist_ok=True)
    LOG_PATH.mkdir(parents=True, exist_ok=True)

settings = Settings()
