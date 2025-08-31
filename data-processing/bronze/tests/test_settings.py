import sys
import importlib


def test_settings_dataset_config(monkeypatch):
    """
    Test that settings.py correctly parses the --storage-account argument
    and populates DATASET_CONFIG paths with the provided storage account.
    """
    test_args = ["program", "--storage-account", "mystorage"]
    monkeypatch.setattr(sys, "argv", test_args)

    settings = importlib.reload(importlib.import_module("src.config.settings"))

    assert settings.storage_account == "mystorage"
    for path in settings.DATASET_CONFIG["input_path"]:
        assert "mystorage" in path
    assert "mystorage" in settings.DATASET_CONFIG["output_path"]
    assert "mystorage" in settings.DATASET_CONFIG["checkpoint_path"]