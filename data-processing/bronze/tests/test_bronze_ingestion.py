import pytest
from unittest.mock import MagicMock, patch
from src.modules import bronze_ingestion


@patch("src.modules.bronze_ingestion.add_metadata_columns")
@patch("src.modules.bronze_ingestion.generate_batch_id", return_value="batch123")
def test_ingest_bronze_customer_data_mock(mock_batch, mock_add_metadata):
    """
    Test that ingest_bronze_customer_data processes the DataFrame correctly
    and calls add_metadata_columns and writeStream with the expected arguments.
    """
    mock_spark = MagicMock()
    mock_df = MagicMock()

    mock_read = MagicMock()
    mock_spark.read = mock_read
    mock_limit_df = MagicMock()
    mock_limit_df.rdd.isEmpty.return_value = False
    mock_read.format.return_value.load.return_value.limit.return_value = mock_limit_df

    mock_readStream = MagicMock()
    mock_readStream.format.return_value = mock_readStream
    mock_readStream.option.side_effect = lambda *args, **kwargs: mock_readStream
    mock_readStream.schema.return_value = mock_readStream
    mock_readStream.load.return_value = mock_df

    mock_spark.readStream = mock_readStream
    mock_add_metadata.return_value = mock_df
    
    mock_query = MagicMock()
    mock_query.awaitTermination.return_value = None
    mock_df.writeStream.format.return_value.outputMode.return_value.trigger.return_value.option.return_value.start.return_value = mock_query

    config = {
        "input_path": "input",
        "output_path": "output",
        "checkpoint_path": "checkpoint",
        "catalog": "mock_catalog",
        "database": "mock_database"
    }
    schema = MagicMock()
    file_format = "csv"

    result = bronze_ingestion.ingest_bronze_customer_data(mock_spark, config, schema, file_format)
    assert result == [mock_query]
    mock_batch.assert_called_once()
    mock_add_metadata.assert_called_once_with(mock_df, "batch123")


def test_ingest_bronze_no_files(spark):
    """
    Tests that ingestion skips path when no files are present.
    """
    schema = MagicMock()
    config = {
        "input_path": ["input"],
        "output_path": "output",
        "checkpoint_path": "checkpoint",
        "catalog": "mock_catalog",
        "database": "mock_database"
    }

    mock_rdd = MagicMock()
    mock_rdd.isEmpty.return_value = True

    spark.read.format.return_value.load.return_value.limit.return_value.rdd = mock_rdd

    result = bronze_ingestion.ingest_bronze_customer_data(
        spark, config, schema, "csv"
    )
    assert result == []


@patch("src.modules.bronze_ingestion.DeltaTable.isDeltaTable", return_value=False)
def test_create_delta_table(mock_is_delta, spark):
    """
    Tests that a Delta table is created if it does not exist.
    """
    schema = MagicMock()
    config = {
        "input_path": "input",
        "output_path": "output",
        "checkpoint_path": "checkpoint",
        "catalog": "mock_catalog",
        "database": "mock_database"
    }

    spark.createDataFrame = MagicMock(return_value=MagicMock(write=MagicMock()))
    result = bronze_ingestion.ingest_bronze_customer_data(
        spark, config, schema, "csv"
    )
    assert result == []
    mock_is_delta.assert_called_once()
