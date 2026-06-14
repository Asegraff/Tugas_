"""Backup Management Module"""

import logging
import shutil
from datetime import datetime
from pathlib import Path
from config.settings import settings

logger = logging.getLogger(__name__)

class BackupManager:
    """Manage system backups"""
    
    def __init__(self):
        self.backup_path = settings.BACKUP_PATH
        self.db_path = settings.DB_PATH
    
    def create_backup(self, description: str = '') -> bool:
        """Create backup of database and Excel files"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_dir = self.backup_path / f"backup_{timestamp}"
            backup_dir.mkdir(parents=True, exist_ok=True)
            
            # Backup database
            if Path(self.db_path).exists():
                shutil.copy2(self.db_path, backup_dir / 'invoice_system.accdb')
                logger.info(f"Database backed up to {backup_dir}")
            
            # Backup Excel file
            excel_path = settings.EXCEL_TEMPLATE_PATH
            if Path(excel_path).exists():
                shutil.copy2(excel_path, backup_dir / 'Master_Dashboard.xlsm')
                logger.info(f"Excel file backed up to {backup_dir}")
            
            # Create metadata file
            metadata_path = backup_dir / 'backup_info.txt'
            with open(metadata_path, 'w') as f:
                f.write(f"Backup Date: {datetime.now().isoformat()}\n")
                f.write(f"Description: {description}\n")
            
            logger.info(f"Backup created successfully: {backup_dir}")
            return True
        except Exception as e:
            logger.error(f"Backup creation failed: {e}")
            return False
    
    def get_backups(self) -> list:
        """List all available backups"""
        try:
            backups = [d for d in self.backup_path.iterdir() if d.is_dir()]
            return sorted(backups, reverse=True)
        except Exception as e:
            logger.error(f"List backups failed: {e}")
            return []
    
    def restore_backup(self, backup_dir: Path) -> bool:
        """Restore from backup"""
        try:
            db_backup = backup_dir / 'invoice_system.accdb'
            excel_backup = backup_dir / 'Master_Dashboard.xlsm'
            
            if db_backup.exists():
                shutil.copy2(db_backup, self.db_path)
                logger.info(f"Database restored from {backup_dir}")
            
            if excel_backup.exists():
                shutil.copy2(excel_backup, settings.EXCEL_TEMPLATE_PATH)
                logger.info(f"Excel file restored from {backup_dir}")
            
            return True
        except Exception as e:
            logger.error(f"Restore failed: {e}")
            return False
    
    def cleanup_old_backups(self, keep_days: int = None) -> bool:
        """Remove backups older than specified days"""
        try:
            keep_days = keep_days or settings.BACKUP_INTERVAL
            from datetime import timedelta
            
            cutoff = datetime.now() - timedelta(days=keep_days)
            backups = self.get_backups()
            
            removed_count = 0
            for backup_dir in backups:
                if backup_dir.stat().st_mtime < cutoff.timestamp():
                    shutil.rmtree(backup_dir)
                    removed_count += 1
            
            logger.info(f"Removed {removed_count} old backups")
            return True
        except Exception as e:
            logger.error(f"Cleanup failed: {e}")
            return False
