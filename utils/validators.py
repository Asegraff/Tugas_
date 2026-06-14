"""Input validation utilities"""

import re
from datetime import datetime

def validate_date(date_str: str, format: str = '%Y-%m-%d') -> bool:
    """Validate date format"""
    try:
        datetime.strptime(date_str, format)
        return True
    except ValueError:
        return False

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Validate phone number"""
    pattern = r'^\+?1?\d{9,15}$'
    return re.match(pattern, phone) is not None

def validate_rig(rig: str) -> bool:
    """Validate rig ID"""
    from config.constants import RIGS
    return rig in RIGS

def validate_category(category: str) -> bool:
    """Validate category"""
    from config.constants import CATEGORIES
    return category in CATEGORIES
