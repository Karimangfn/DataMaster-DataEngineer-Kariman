import sys
import importlib
import pytest


def test_dataset_config_keys(monkeypatch):
    """
    Tests if the DATASET_CONFIG dictionary contains all required keys
    for the Gold pipeline and if their values are strings.
    """
    test_args = [
        "program",
        "--storage-account", "mystorage",
        "--catalog", "mock_catalog",
        "--database", "mock_database"
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    settings = importlib.reload(importlib.import_module("src.config.settings"))

    required_keys = ["silver_path", "gold_path", "catalog", "database"]
    for key in required_keys:
        assert key in settings.DATASET_CONFIG
        assert isinstance(settings.DATASET_CONFIG[key], str)
