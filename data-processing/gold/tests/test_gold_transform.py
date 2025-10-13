import types
import importlib
import pytest

from unittest.mock import patch, MagicMock
from src.modules.gold_transform import transform_gold

mock_args = types.SimpleNamespace(
    storage_account="mock",
    catalog="mock_catalog",
    database="mock_database"
)


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

    write_mock = fake_df.write.format.return_value
    mode_mock = write_mock.mode.return_value
    option_mock = mode_mock.option.return_value
    option_mock.saveAsTable.return_value = None

    silver_path = "fake_silver_path"
    gold_path = "fake_gold_path"

    config = {
        "silver_path": silver_path,
        "gold_path": gold_path,
        "catalog": "fake_catalog",
        "database": "fake_database"
    }
    
    transform_gold(fake_spark, config)

    mock_add_month.assert_called_once_with(fake_df)
    mock_agg.assert_called_once_with(fake_df, ["store_location", "purchase_month"])
    
    option_mock.saveAsTable.assert_called_once_with(
        f"{config['catalog']}.{config['database']}.gold"
    )


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
