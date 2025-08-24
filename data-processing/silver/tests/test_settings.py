import pytest
from src.config.settings import DATASET_CONFIG


def test_dataset_config_keys():
    """
    Test that DATASET_CONFIG contains all required keys.
    """
    required_keys = ["bronze_path", "silver_path", "silver_checkpoint_path"]
    for key in required_keys:
        assert key in DATASET_CONFIG
        assert isinstance(DATASET_CONFIG[key], str)


def test_dataset_config_paths_format():
    """
    Test that paths in DATASET_CONFIG are valid non-empty strings.
    """
    for key, path in DATASET_CONFIG.items():
        assert path.startswith("abfss://")
        assert path.endswith("/")
        assert len(path) > len("abfss://")
