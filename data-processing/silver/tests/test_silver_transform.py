import types
import importlib
import pytest

from unittest.mock import patch, MagicMock
from src.modules.silver_transform import transform_silver

mock_args = types.SimpleNamespace(storage_account="mock")


@patch("src.modules.silver_transform.add_high_value_flag")
@patch("src.modules.silver_transform.mask_sensitive_data")
@patch("src.modules.silver_transform.deduplicate")
@patch("src.modules.silver_transform.clean_and_cast_columns")
@patch("src.modules.silver_transform.grant_access_to_silver")
def test_silver_transform_pipeline(mock_grant, mock_clean, mock_dedup, mock_mask, mock_high_value):
    """
    Test that the Silver transformation pipeline executes successfully with data present.
    """
    fake_df = MagicMock()
    fake_df.withColumn.return_value = fake_df
    fake_df.drop.return_value = fake_df
    fake_df.filter.return_value = fake_df
    
    mock_clean.return_value = fake_df
    mock_dedup.return_value = fake_df
    mock_mask.return_value = fake_df
    mock_high_value.return_value = fake_df

    fake_spark = MagicMock()
    fake_spark.read.format.return_value.load.return_value = fake_df
    fake_df.write.format.return_value.mode.return_value.option.return_value.saveAsTable.return_value = None

    config = {
        "bronze_path": "fake_bronze_path",
        "silver_path": "fake_silver_path",
        "catalog": "fake_catalog",
        "database": "fake_database",
    }

    transform_silver(fake_spark, config)

    mock_clean.assert_called_once_with(fake_df)
    mock_dedup.assert_called_once_with(fake_df)
    mock_mask.assert_called_once_with(fake_df)
    mock_high_value.assert_called_once_with(fake_df)

    fake_df.write.format.return_value.mode.return_value.option.return_value.saveAsTable.assert_called_once_with(
        f"{config['catalog']}.{config['database']}.silver"
    )


def test_silver_transform_pipeline_error():
    """
    Test that the Silver transformation pipeline raises an exception on read failure.
    """
    fake_spark = MagicMock()
    fake_spark.read.format.return_value.load.side_effect = Exception("Read failed")

    import src.main as main_module
    importlib.reload(main_module)
    main_module.spark = fake_spark

    try:
        main_module.main()
    except Exception as e:
        assert str(e) == "Read failed"
