import pytest
from src.application.helpers.serialization import convert_to_json
from src.domain.exceptions.exceptions import JSONConversionError


def test_convert_to_json_success():
    json_str = '{"key": "value", "num": 123}'
    result = convert_to_json(json_str)
    assert result["key"] == "value"
    assert result["num"] == 123


def test_convert_to_json_invalid():
    bad_json = '{"key": value without quotes}'
    with pytest.raises(JSONConversionError):
        convert_to_json(bad_json)
