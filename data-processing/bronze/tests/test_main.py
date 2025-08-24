import sys
import types
import importlib
from unittest.mock import patch, MagicMock

mock_args = types.SimpleNamespace(storage_account="mock")


def test_main_pipeline():
    """
    Tests if main.py executes correctly when files are present.
    """
    fake_file = types.SimpleNamespace(name="data.csv")
    fake_dbutils = types.SimpleNamespace(fs=types.SimpleNamespace(ls=lambda _: [fake_file]))
    
    with patch("argparse.ArgumentParser.parse_args", return_value=mock_args):
        import src.main as main_module
        importlib.reload(main_module)

        main_module.dbutils = fake_dbutils
        main_module.spark = MagicMock()

        main_module.ingest_bronze_customer_data = MagicMock(return_value="done")
        main_module.detect_format_from_extension = MagicMock(return_value="csv")
        main_module.get_customer_schema = MagicMock(return_value="schema")

        main_module.main()
        main_module.ingest_bronze_customer_data.assert_called_once()


def test_main_pipeline_no_files():
    """
    Tests if main.py exits correctly when no files are found in the input path.
    """
    fake_dbutils = types.SimpleNamespace(fs=types.SimpleNamespace(ls=lambda _: []))
    
    with patch("argparse.ArgumentParser.parse_args", return_value=mock_args):
        import src.main as main_module
        importlib.reload(main_module)

        main_module.dbutils = fake_dbutils
        main_module.spark = MagicMock()

        result = main_module.main()
        assert result is None
