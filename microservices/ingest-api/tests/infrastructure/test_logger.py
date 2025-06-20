import logging
import logging.config
import sys

from src.infrastructure.logging.logging_config import LOGGING_CONFIG
from src.infrastructure.logging.logging_setup import get_logger, setup_logging


def test_get_logger_returns_logger_instance():
    """
    Test that get_logger returns an instance of logging.Logger.
    """
    setup_logging()
    logger = get_logger("myapp")
    assert isinstance(logger, logging.Logger)


def test_get_logger_sets_level_and_handler():
    """
    Test that get_logger sets level, stream handler, formatter,
    and disables propagation.
    """
    setup_logging()
    logger_name = "myapp"
    logger = logging.getLogger(logger_name)
    logger.handlers.clear()

    logging.config.dictConfig(LOGGING_CONFIG)
    result_logger = get_logger(logger_name)

    assert result_logger.level == logging.INFO
    assert len(result_logger.handlers) == 1

    handler = result_logger.handlers[0]
    assert isinstance(handler, logging.StreamHandler)
    assert handler.stream == sys.stdout
    assert isinstance(handler.formatter, logging.Formatter)
    assert "%(asctime)s" in handler.formatter._fmt
    assert result_logger.propagate is False


def test_get_logger_does_not_add_duplicate_handlers():
    """
    Test that get_logger does not add duplicate handlers when called
    multiple times.
    """
    setup_logging()
    logger_name = "myapp"
    logger = logging.getLogger(logger_name)
    logger.handlers.clear()

    logging.config.dictConfig(LOGGING_CONFIG)
    get_logger(logger_name)
    first_count = len(logger.handlers)

    get_logger(logger_name)
    second_count = len(logger.handlers)

    assert first_count == 1
    assert second_count == 1
