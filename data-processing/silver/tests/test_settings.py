import sys
import importlib
import pytest


def test_dataset_config_keys(monkeypatch):
    """
    Test that DATASET_CONFIG contains all required keys.
    """
    test_args = [
        "program",
        "--storage-account", "mystorage",
        "--catalog", "mock_catalog",
        "--database", "mock_database"
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    settings = importlib.reload(importlib.import_module("src.config.settings"))

    required_keys = ["bronze_path", "silver_path"]
    for key in required_keys:
        assert key in settings.DATASET_CONFIG
        assert isinstance(settings.DATASET_CONFIG[key], str)


def test_dataset_config_paths_format(monkeypatch):
    """
    Test that paths in DATASET_CONFIG are valid non-empty strings.
    """
    test_args = [
        "program",
        "--storage-account", "mystorage",
        "--catalog", "mock_catalog",
        "--database", "mock_database"
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    settings = importlib.reload(importlib.import_module("src.config.settings"))

    path_keys = ["bronze_path", "silver_path"]
    for key in path_keys:
        path = settings.DATASET_CONFIG[key]
        assert path.startswith("abfss://")
        assert path.endswith("/")
        assert len(path) > len("abfss://")
