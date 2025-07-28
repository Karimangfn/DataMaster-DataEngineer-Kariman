import json
from typing import Any

from src.domain.exceptions.exceptions import JSONConversionError
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


def load_json(response_text: str) -> Any:
    """
    Parse a JSON-formatted string into a Python object.

    Args:
        response_text (str): Raw JSON string returned by the API.

    Returns:
        Any: Python object parsed from the JSON string.

    Raises:
        JSONConversionError: If the input string cannot be parsed
        as valid JSON.
    """
    try:
        result = json.loads(response_text)
        logger.debug(
            "Successfully converted response text to JSON."
        )
        return result
    except json.JSONDecodeError as e:
        logger.error(
            "Failed to convert response text to JSON.",
            exc_info=True
        )
        raise JSONConversionError(
            f"Failed to convert JSON: {str(e)}"
        )
