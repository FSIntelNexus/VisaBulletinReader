import logging
import sys
import os

def setup_logging(name=__name__):
    """
    Configures logging for the application.
    Logs to stdout for compatibility with cloud platforms like Vercel and Google Cloud Run.
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
    return logger
