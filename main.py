#!/usr/bin/env python
"""Main application entry point"""

import logging
import sys
from pathlib import Path

# Setup path
sys.path.insert(0, str(Path(__file__).parent))

from utils.logger import setup_logger
from config.settings import settings
from ui.cli import CLI

logger = setup_logger('main')

def main():
    """Main application entry"""
    logger.info("="*50)
    logger.info("Sistem Invoice & Rekap ACU")
    logger.info("="*50)
    
    try:
        # Initialize CLI
        cli = CLI()
        cli.run()
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Application error: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
