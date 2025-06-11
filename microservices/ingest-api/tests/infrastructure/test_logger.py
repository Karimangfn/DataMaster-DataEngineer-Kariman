import logging
import sys

from src.infrastructure.logging.logger import get_logger


def test_get_logger_returns_logger_instance():
    """
    Test that get_logger returns an instance of logging.Logger.
    """
    logger = get_logger("test_logger")
    assert isinstance(logger, logging.Logger)


def test_get_logger_sets_level_and_handler():
    """
    Test that get_logger sets level, stream handler, formatter,
    and disables propagation.
    """
    logger_name = "custom_logger_test"
    logger = logging.getLogger(logger_name)
    logger.handlers.clear()

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
    logger_name = "no_duplicates_logger"
    logger = logging.getLogger(logger_name)
    logger.handlers.clear()

    get_logger(logger_name)
    first_count = len(logger.handlers)

    get_logger(logger_name)
    second_count = len(logger.handlers)

    assert first_count == 1
    assert second_count == 1
