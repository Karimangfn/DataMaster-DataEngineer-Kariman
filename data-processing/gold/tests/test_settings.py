import sys
import importlib
import pytest


def test_dataset_config_keys(monkeypatch):
    """
    Tests if the DATASET_CONFIG dictionary contains all required keys
    for the Gold pipeline and if their values are strings.
    """
    test_args = ["program", "--storage-account", "mystorage"]
    monkeypatch.setattr(sys, "argv", test_args)

    settings = importlib.reload(importlib.import_module("src.config.settings"))

    required_keys = ["silver_path", "gold_path"]
    for key in required_keys:
        assert key in settings.DATASET_CONFIG
        assert isinstance(settings.DATASET_CONFIG[key], str)
