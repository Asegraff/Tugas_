"""User Management Module"""

import logging
import hashlib
from datetime import datetime
from database import AccessDatabase
from database.queries import DatabaseQueries
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class UserManager:
    """Manage users and authentication"""
    
    def __init__(self):
        self.db = AccessDatabase()
        self.queries = DatabaseQueries()
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_user(self, username: str, password: str, role: str) -> bool:
        """Create new user"""
        try:
            # Check if user exists
            with self.db:
                existing = self.db.execute_query(
                    self.queries.GET_USER_BY_USERNAME,
                    (username,)
                )
            
            if existing:
                logger.warning(f"User {username} already exists")
                return False
            
            hashed_password = self.hash_password(password)
            created_date = datetime.now().isoformat()
            params = (username, hashed_password, role, created_date)
            
            with self.db:
                result = self.db.execute_update(self.queries.INSERT_USER, params)
            
            if result:
                logger.info(f"User {username} created with role {role}")
            return result
        except Exception as e:
            logger.error(f"Create user failed: {e}")
            return False
    
    def authenticate(self, username: str, password: str) -> Optional[Dict]:
        """Authenticate user"""
        try:
            with self.db:
                results = self.db.execute_query(
                    self.queries.GET_USER_BY_USERNAME,
                    (username,)
                )
            
            if not results:
                logger.warning(f"User {username} not found")
                return None
            
            user = results[0]
            hashed_password = self.hash_password(password)
            
            if user['Password'] == hashed_password:
                logger.info(f"User {username} authenticated successfully")
                return user
            else:
                logger.warning(f"Invalid password for user {username}")
                return None
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            return None
    
    def change_password(self, user_id: int, new_password: str) -> bool:
        """Change user password"""
        try:
            hashed_password = self.hash_password(new_password)
            updated_date = datetime.now().isoformat()
            params = (hashed_password, 'OPERATOR', updated_date, user_id)
            
            with self.db:
                result = self.db.execute_update(self.queries.UPDATE_USER, params)
            
            if result:
                logger.info(f"Password changed for user ID {user_id}")
            return result
        except Exception as e:
            logger.error(f"Change password failed: {e}")
            return False
    
    def get_all_users(self) -> List[Dict]:
        """Get all users"""
        try:
            with self.db:
                results = self.db.execute_query(self.queries.GET_ALL_USERS)
            return results
        except Exception as e:
            logger.error(f"Get users failed: {e}")
            return []
