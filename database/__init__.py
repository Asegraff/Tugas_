"""Database module for Invoice System"""

from .connection import AccessDatabase
from .queries import DatabaseQueries

__all__ = ['AccessDatabase', 'DatabaseQueries']
