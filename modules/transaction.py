"""Transaction Management Module"""

import logging
from datetime import datetime
from decimal import Decimal
from database import AccessDatabase
from database.queries import DatabaseQueries
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class TransactionManager:
    """Manage daily transactions"""
    
    def __init__(self):
        self.db = AccessDatabase()
        self.queries = DatabaseQueries()
    
    def add_transaction(self, tanggal: str, rig: str, kategori: str, 
                       qty_pax: int, harga: Decimal) -> bool:
        """Add new daily transaction"""
        try:
            total = qty_pax * float(harga)
            params = (tanggal, rig, kategori, qty_pax, harga, total)
            
            with self.db:
                result = self.db.execute_update(self.queries.INSERT_TRANSACTION, params)
            
            if result:
                logger.info(f"Transaction added: {rig} - {kategori} on {tanggal}")
            return result
        except Exception as e:
            logger.error(f"Add transaction failed: {e}")
            return False
    
    def update_transaction(self, transaction_id: int, tanggal: str, rig: str, 
                          kategori: str, qty_pax: int, harga: Decimal) -> bool:
        """Update existing transaction"""
        try:
            total = qty_pax * float(harga)
            params = (tanggal, rig, kategori, qty_pax, harga, total, transaction_id)
            
            with self.db:
                result = self.db.execute_update(self.queries.UPDATE_TRANSACTION, params)
            
            if result:
                logger.info(f"Transaction {transaction_id} updated")
            return result
        except Exception as e:
            logger.error(f"Update transaction failed: {e}")
            return False
    
    def delete_transaction(self, transaction_id: int) -> bool:
        """Delete transaction"""
        try:
            with self.db:
                result = self.db.execute_update(self.queries.DELETE_TRANSACTION, (transaction_id,))
            
            if result:
                logger.info(f"Transaction {transaction_id} deleted")
            return result
        except Exception as e:
            logger.error(f"Delete transaction failed: {e}")
            return False
    
    def get_transactions_by_period(self, start_date: str, end_date: str) -> List[Dict]:
        """Get transactions for a period"""
        try:
            with self.db:
                results = self.db.execute_query(
                    self.queries.GET_TRANSACTIONS_BY_PERIOD,
                    (start_date, end_date)
                )
            return results
        except Exception as e:
            logger.error(f"Get transactions failed: {e}")
            return []
    
    def get_transactions_by_rig(self, rig: str) -> List[Dict]:
        """Get transactions for a specific rig"""
        try:
            with self.db:
                results = self.db.execute_query(
                    self.queries.GET_TRANSACTIONS_BY_RIG,
                    (rig,)
                )
            return results
        except Exception as e:
            logger.error(f"Get transactions failed: {e}")
            return []
    
    def get_summary_by_period(self, start_date: str, end_date: str) -> List[Dict]:
        """Get summary by period"""
        try:
            with self.db:
                results = self.db.execute_query(
                    self.queries.GET_SUMMARY_BY_RIG_PERIOD,
                    (start_date, end_date)
                )
            return results
        except Exception as e:
            logger.error(f"Get summary failed: {e}")
            return []
