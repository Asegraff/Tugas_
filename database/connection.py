"""Database Connection Module"""

import pyodbc
import logging
from config.settings import settings
from typing import List, Dict, Tuple

logger = logging.getLogger(__name__)

class AccessDatabase:
    """Manager for Microsoft Access Database connections"""
    
    def __init__(self, db_path: str = None, driver: str = None):
        self.db_path = db_path or settings.DB_PATH
        self.driver = driver or settings.DB_DRIVER
        self.connection = None
        
    def connect(self) -> bool:
        """Establish database connection"""
        try:
            conn_str = f'Driver={{{self.driver}}};DBQ={self.db_path};'
            self.connection = pyodbc.connect(conn_str)
            logger.info(f"Database connected: {self.db_path}")
            return True
        except pyodbc.Error as e:
            logger.error(f"Database connection failed: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            logger.info("Database disconnected")
    
    def execute_query(self, query: str, params: Tuple = None) -> List[Dict]:
        """Execute SELECT query"""
        if not self.connection:
            self.connect()
        
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            columns = [description[0] for description in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            return results
        except pyodbc.Error as e:
            logger.error(f"Query execution failed: {e}")
            return []
    
    def execute_update(self, query: str, params: Tuple = None) -> bool:
        """Execute INSERT/UPDATE/DELETE query"""
        if not self.connection:
            self.connect()
        
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
            logger.info(f"Update executed successfully")
            return True
        except pyodbc.Error as e:
            self.connection.rollback()
            logger.error(f"Update execution failed: {e}")
            return False
    
    def execute_batch(self, query: str, data: List[Tuple]) -> bool:
        """Execute batch INSERT/UPDATE operations"""
        if not self.connection:
            self.connect()
        
        try:
            cursor = self.connection.cursor()
            cursor.executemany(query, data)
            self.connection.commit()
            cursor.close()
            logger.info(f"Batch execution: {len(data)} records processed")
            return True
        except pyodbc.Error as e:
            self.connection.rollback()
            logger.error(f"Batch execution failed: {e}")
            return False
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
