import json
from typing import Any

from src.domain.exceptions.exceptions import JSONConversionError
from src.infrastructure.logging.logging_setup import get_logger

logger = get_logger(__name__)


def convert_to_json(response_text: str) -> Any:
    """
    Convert API response text to JSON.

    Args:
        response_text (str): Raw text returned by the API.

    Returns:
        Any: Parsed JSON content.

    Raises:
        JSONConversionError: If the response text cannot be parsed into JSON.
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
