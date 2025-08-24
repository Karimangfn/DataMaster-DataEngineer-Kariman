import re
import pytest
from unittest.mock import MagicMock, patch
from src.utils.utils import generate_batch_id, detect_format_from_extension, add_metadata_columns


def test_generate_batch_id_format():
    """
    Test that generate_batch_id returns a valid UUID string.
    """
    batch_id = generate_batch_id()
    assert re.match(r"^[0-9a-f-]{36}$", batch_id)

@pytest.mark.parametrize("file_name,expected", [
    ("data.csv", "csv"),
    ("records.json", "json"),
    ("table.parquet", "parquet"),
])
def test_detect_format_from_extension_valid(file_name, expected):
    """
    Test that detect_format_from_extension correctly identifies supported file formats.
    """
    assert detect_format_from_extension(file_name) == expected

def test_detect_format_from_extension_invalid():
    """
    Test that detect_format_from_extension raises ValueError for unsupported extensions.
    """
    with pytest.raises(ValueError):
        detect_format_from_extension("data.txt")


@patch("src.utils.utils.input_file_name", return_value="file.csv")
@patch("src.utils.utils.current_timestamp", return_value="2025-08-24T00:00:00")
@patch("src.utils.utils.lit", side_effect=lambda x: x)
def test_add_metadata_columns(mock_lit, mock_ts, mock_file):
    """
    Test that add_metadata_columns adds metadata columns correctly using mocked Spark functions.
    """
    mock_df = MagicMock()
    mock_df.withColumn.return_value = mock_df
    batch_id = "1234"

    result_df = add_metadata_columns(mock_df, batch_id)

    assert mock_df.withColumn.call_count == 3
    assert result_df == mock_df