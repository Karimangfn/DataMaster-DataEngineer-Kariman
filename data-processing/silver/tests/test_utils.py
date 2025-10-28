import re
import pytest
from unittest.mock import MagicMock, patch
from src.utils.utils import (
    clean_and_cast_columns,
    deduplicate,
    mask_sensitive_data,
    add_high_value_flag,
    validate_email
)


@patch("src.utils.utils.coalesce")
@patch("src.utils.utils.regexp_replace")
@patch("src.utils.utils.to_date")
@patch("src.utils.utils.col")
def test_clean_and_cast_columns(mock_col, mock_to_date, mock_regexp_replace, mock_coalesce):
    """
    Test that clean_and_cast_columns casts purchase_date and total_amount correctly.
    """
    df = MagicMock()
    col_mock = MagicMock()
    col_mock.cast.return_value = col_mock

    mock_col.side_effect = lambda x: col_mock
    mock_to_date.side_effect = lambda c, fmt: c
    mock_regexp_replace.side_effect = lambda c, p, r: c
    mock_coalesce.side_effect = lambda *args: args[0]

    df.withColumn.return_value = df

    result_df = clean_and_cast_columns(df)

    assert df.withColumn.call_count >= 2
    assert result_df == df


@patch("src.utils.utils.col")
@patch("src.utils.utils.Window")
@patch("src.utils.utils.row_number")
def test_deduplicate(mock_row_number, mock_window, mock_col):
    """
    Test that deduplicate adds row_number and filters correctly.
    """
    df = MagicMock()
    df.withColumn.return_value = df
    df.filter.return_value = df
    df.drop.return_value = df

    col_mock = MagicMock()
    col_mock.desc.return_value = "desc_mock"
    mock_col.side_effect = lambda x: col_mock

    window_mock = MagicMock()
    mock_window.partitionBy.return_value.orderBy.return_value = window_mock

    row_number_mock = MagicMock()
    mock_row_number.return_value.over.return_value = "row_number_mock"

    result_df = deduplicate(df)

    assert df.withColumn.call_count == 1
    assert df.filter.call_count == 1
    assert df.drop.call_count == 1
    assert result_df == df


@patch("src.utils.utils.sha2")
@patch("src.utils.utils.col")
def test_mask_sensitive_data(mock_col, mock_sha2):
    """
    Test that mask_sensitive_data adds hashed columns and drops originals.
    """
    df = MagicMock()
    df.withColumn.return_value = df
    df.drop.return_value = df

    mock_col.side_effect = lambda x: x
    mock_sha2.side_effect = lambda c, l: c

    result_df = mask_sensitive_data(df)

    assert df.withColumn.call_count == 2
    assert df.drop.call_count == 2
    assert result_df == df


@patch("src.utils.utils.col")
def test_add_high_value_flag(mock_col):
    """
    Test that add_high_value_flag adds high_value_purchase boolean column.
    """
    df = MagicMock()
    col_mock = MagicMock()
    col_mock.__gt__.return_value = col_mock
    col_mock.cast.return_value = col_mock
    mock_col.side_effect = lambda x: col_mock
    df.withColumn.return_value = df

    result_df = add_high_value_flag(df, threshold=100)

    df.withColumn.assert_called_once()
    assert result_df == df


@patch("src.utils.utils.udf")
@patch("src.utils.utils.col")
def test_validate_email(mock_col, mock_udf):
    """
    Test that validate_email adds is_email_valid column.
    """
    df = MagicMock()
    df.__getitem__.return_value = "mock_email"
    df.withColumn.return_value = df

    mock_col.side_effect = lambda x: x
    mock_udf.side_effect = lambda f, t: f

    result_df = validate_email(df)

    df.withColumn.assert_called_once()
    assert result_df == df
