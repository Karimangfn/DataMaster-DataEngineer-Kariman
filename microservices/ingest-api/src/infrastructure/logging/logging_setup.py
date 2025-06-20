import logging
import logging.config

from src.infrastructure.logging.logging_config import LOGGING_CONFIG


def setup_logging():
    """
    Configure the Python logging module using the LOGGING_CONFIG dictionary.
    """
    logging.config.dictConfig(LOGGING_CONFIG)


def get_logger(name: str) -> logging.Logger:
    """
    Retrieve a logger instance with the specified name.

    Args:
        name (str): The name of the logger, usually __name__ of the module.

    Returns:
        logging.Logger: Configured logger instance according to LOGGING_CONFIG.
    """
    return logging.getLogger(name)
