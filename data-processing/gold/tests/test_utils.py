import pytest
from unittest.mock import MagicMock, patch
from src.utils.utils import add_purchase_month_column, aggregate_purchase_metrics


@patch("src.utils.utils.date_format")
@patch("src.utils.utils.col")
def test_add_purchase_month_column(mock_col, mock_date_format):
    """
    Test that add_purchase_month_column adds the purchase_month column correctly.
    """
    df = MagicMock()
    df.withColumn.return_value = df

    mock_col.side_effect = lambda x: x
    mock_date_format.side_effect = lambda c, fmt: c

    result_df = add_purchase_month_column(df)

    df.withColumn.assert_called_once()
    assert result_df == df


@patch("src.utils.utils.count")
@patch("src.utils.utils._sum")
@patch("src.utils.utils.avg")
@patch("src.utils.utils.expr")
def test_aggregate_purchase_metrics(mock_expr, mock_avg, mock_sum, mock_count):
    """
    Test that aggregate_purchase_metrics aggregates columns correctly.
    """
    df = MagicMock()
    df.groupBy.return_value.agg.return_value = df

    def make_mock(x):
        m = MagicMock()
        m.alias.return_value = m
        return m

    mock_count.side_effect = make_mock
    mock_sum.side_effect = make_mock
    mock_avg.side_effect = make_mock
    mock_expr.side_effect = make_mock

    group_cols = ["store_location", "purchase_month"]

    result_df = aggregate_purchase_metrics(df, group_cols)

    df.groupBy.assert_called_once_with(*group_cols)
    df.groupBy.return_value.agg.assert_called_once()
    assert result_df == df
