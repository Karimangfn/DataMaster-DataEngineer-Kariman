import json
from typing import Any

from src.domain.exceptions.exceptions import JSONConversionError


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
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        raise JSONConversionError(e)
