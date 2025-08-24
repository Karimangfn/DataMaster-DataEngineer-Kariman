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

    mock_readStream = MagicMock()
    mock_readStream.format.return_value = mock_readStream
    mock_readStream.option.side_effect = lambda *args, **kwargs: mock_readStream
    mock_readStream.schema.return_value = mock_readStream
    mock_readStream.load.return_value = mock_df

    mock_spark.readStream = mock_readStream
    mock_add_metadata.return_value = mock_df
    mock_df.writeStream.format.return_value.outputMode.return_value.trigger.return_value.option.return_value.start.return_value = "stream_query"

    config = {
        "input_path": "input",
        "output_path": "output",
        "checkpoint_path": "checkpoint"
    }
    schema = MagicMock()
    file_format = "csv"

    result = bronze_ingestion.ingest_bronze_customer_data(mock_spark, config, schema, file_format)
    assert result == "stream_query"
    mock_batch.assert_called_once()
    mock_add_metadata.assert_called_once_with(mock_df, "batch123")
