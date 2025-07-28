import pytest
from src.application.helpers.serialization import load_json
from src.domain.exceptions.exceptions import JSONConversionError


def test_load_json_success():
    """
    Test that a valid JSON string is correctly converted to
    a Python dictionary.
    """
    json_str = '{"key": "value", "num": 123}'
    result = load_json(json_str)
    assert result["key"] == "value"
    assert result["num"] == 123


def test_load_json_invalid():
    """
    Test that an invalid JSON string raises a JSONConversionError.
    """
    bad_json = '{"key": value without quotes}'
    with pytest.raises(JSONConversionError):
        load_json(bad_json)
