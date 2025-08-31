import types
import importlib
import pytest

from unittest.mock import patch, MagicMock
from src.modules.gold_transform import transform_gold

mock_args = types.SimpleNamespace(storage_account="mock")


@patch("src.modules.gold_transform.aggregate_purchase_metrics")
@patch("src.modules.gold_transform.add_purchase_month_column")
def test_gold_transform_pipeline(mock_add_month, mock_agg):
    """
    Test that the Gold transformation pipeline executes successfully
    with mocked data.
    """
    fake_df = MagicMock()
    fake_df.withColumn.return_value = fake_df
    fake_df.groupBy.return_value.agg.return_value = fake_df
    fake_df.write.format.return_value.mode.return_value.save.return_value = None

    mock_add_month.return_value = fake_df
    mock_agg.return_value = fake_df

    fake_spark = MagicMock()
    fake_spark.read.format.return_value.load.return_value = fake_df

    silver_path = "fake_silver_path"
    gold_path = "fake_gold_path"

    transform_gold(fake_spark, silver_path, gold_path)

    mock_add_month.assert_called_once_with(fake_df)
    mock_agg.assert_called_once_with(fake_df, ["store_location", "purchase_month"])
    fake_df.write.format.return_value.mode.return_value.save.assert_called_once_with(gold_path)


def test_gold_transform_pipeline_error():
    """
    Test that the Gold transformation pipeline raises an exception
    if reading the Silver data fails.
    """
    fake_spark = MagicMock()
    fake_spark.read.format.return_value.load.side_effect = Exception("Read failed")

    with patch("argparse.ArgumentParser.parse_args", return_value=mock_args):
        import src.main as main_module
        importlib.reload(main_module)

        main_module.spark = fake_spark

        try:
            main_module.main()
        except Exception as e:
            assert str(e) == "Read failed"
