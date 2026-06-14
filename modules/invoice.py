"""Invoice Management Module"""

import logging
from datetime import datetime
from decimal import Decimal
from database import AccessDatabase
from database.queries import DatabaseQueries
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class InvoiceManager:
    """Manage invoices"""
    
    def __init__(self):
        self.db = AccessDatabase()
        self.queries = DatabaseQueries()
    
    def generate_invoice_number(self, rig: str, period: str) -> str:
        """Generate invoice number format: INV-RIG-YYYY-MM"""
        return f"INV-{rig}-{period.replace('-', '')}"
    
    def create_invoice(self, rig: str, periode: str, nilai_invoice: Decimal) -> bool:
        """Create new invoice"""
        try:
            no_invoice = self.generate_invoice_number(rig, periode)
            status = 'DRAFT'
            created_date = datetime.now().isoformat()
            
            params = (no_invoice, rig, periode, nilai_invoice, status, created_date)
            
            with self.db:
                result = self.db.execute_update(self.queries.INSERT_INVOICE, params)
            
            if result:
                logger.info(f"Invoice created: {no_invoice}")
            return result
        except Exception as e:
            logger.error(f"Create invoice failed: {e}")
            return False
    
    def update_invoice_status(self, invoice_id: int, status: str) -> bool:
        """Update invoice status"""
        try:
            updated_date = datetime.now().isoformat()
            # Get current value first
            with self.db:
                invoice = self.db.execute_query(
                    "SELECT NilaiInvoice FROM Invoice WHERE ID_Invoice = ?",
                    (invoice_id,)
                )
            
            if not invoice:
                return False
            
            nilai = invoice[0]['NilaiInvoice']
            params = (nilai, status, updated_date, invoice_id)
            
            with self.db:
                result = self.db.execute_update(self.queries.UPDATE_INVOICE, params)
            
            if result:
                logger.info(f"Invoice {invoice_id} status updated to {status}")
            return result
        except Exception as e:
            logger.error(f"Update invoice status failed: {e}")
            return False
    
    def get_invoices_by_period(self, periode: str) -> List[Dict]:
        """Get all invoices for a period"""
        try:
            with self.db:
                results = self.db.execute_query(
                    self.queries.GET_INVOICE_BY_PERIOD,
                    (periode,)
                )
            return results
        except Exception as e:
            logger.error(f"Get invoices failed: {e}")
            return []
    
    def get_invoice_by_rig_period(self, rig: str, periode: str) -> Optional[Dict]:
        """Get invoice for specific rig and period"""
        try:
            with self.db:
                results = self.db.execute_query(
                    self.queries.GET_INVOICE_BY_RIG_PERIOD,
                    (rig, periode)
                )
            return results[0] if results else None
        except Exception as e:
            logger.error(f"Get invoice failed: {e}")
            return None
    
    def delete_invoice(self, invoice_id: int) -> bool:
        """Delete invoice"""
        try:
            with self.db:
                result = self.db.execute_update(self.queries.DELETE_INVOICE, (invoice_id,))
            
            if result:
                logger.info(f"Invoice {invoice_id} deleted")
            return result
        except Exception as e:
            logger.error(f"Delete invoice failed: {e}")
            return False
