from unittest.mock import patch
import importlib


def test_main_calls_transform_gold(spark):
    """
    Test that main() calls transform_gold with the correct SparkSession and paths.
    """
    with patch("argparse.ArgumentParser.parse_args") as mock_parse:
        mock_parse.return_value.storage_account = "mock"

        import src.main as main_module
        importlib.reload(main_module)

        with patch.object(main_module, "transform_gold", return_value=None) as mock_transform:
            main_module.spark = spark

            main_module.main()

            mock_transform.assert_called_once_with(
                spark,
                main_module.DATASET_CONFIG
            )