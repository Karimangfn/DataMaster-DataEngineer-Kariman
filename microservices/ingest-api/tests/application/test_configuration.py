from unittest.mock import mock_open, patch

import pytest
import yaml
from src.application.helpers.configuration import load_config
from src.domain.exceptions.exceptions import ConfigurationLoadError


def test_load_config_success():
    fake_yaml = "key: value\nanother: 123"
    m = mock_open(read_data=fake_yaml)

    with patch("builtins.open", m), \
         patch(
            "yaml.safe_load",
            return_value={"key": "value", "another": 123}
         ):
        config = load_config("config.yaml")
        assert config["key"] == "value"
        assert config["another"] == 123


def test_load_config_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        with pytest.raises(ConfigurationLoadError):
            load_config("nonexistent.yaml")


def test_load_config_invalid_yaml():
    m = mock_open(read_data=": invalid yaml")
    with patch("builtins.open", m), \
         patch("yaml.safe_load", side_effect=yaml.YAMLError):
        with pytest.raises(ConfigurationLoadError):
            load_config("bad.yaml")
