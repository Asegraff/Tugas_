"""Output formatting utilities"""

from datetime import datetime
from decimal import Decimal

def format_currency(amount: Decimal, currency: str = 'IDR') -> str:
    """Format amount as currency"""
    if currency == 'IDR':
        return f"{amount:,.0f} IDR"
    else:
        return f"{currency} {amount:,.2f}"

def format_date(date_obj, format: str = '%d-%m-%Y') -> str:
    """Format date object to string"""
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime(format)

def parse_date(date_str: str, format: str = '%Y-%m-%d') -> datetime:
    """Parse date string to datetime object"""
    return datetime.strptime(date_str, format)

def format_percentage(value: float, decimals: int = 2) -> str:
    """Format percentage"""
    return f"{value:.{decimals}f}%"
