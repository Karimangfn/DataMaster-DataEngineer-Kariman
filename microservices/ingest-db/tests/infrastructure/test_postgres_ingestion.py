from unittest.mock import MagicMock

import pytest
from src.domain.exceptions.exceptions import DatabaseIngestionError
from src.infrastructure.ingestion.postgres_ingestion import PostgresIngestion


@pytest.fixture
def mock_connection():
    """
    Fixture that returns a mock PostgreSQL connection and cursor.
    """
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [{"id": 1, "name": "Test"}]
    return mock_conn, mock_cursor


@pytest.fixture
def mock_conn_strategy(mock_connection):
    """
    Fixture that returns a mock connection strategy.
    """
    mock_strategy = MagicMock()
    mock_strategy.get_connection.return_value = mock_connection[0]
    return mock_strategy


@pytest.fixture
def query():
    """
    Fixture that returns a sample SQL query.
    """
    return "SELECT * FROM users;"


def test_ingest_success(mock_conn_strategy, query, mock_connection):
    """
    Test that ingest returns the result of a successful query.
    """
    ingestion = PostgresIngestion(mock_conn_strategy, query)
    result = ingestion.ingest()

    mock_conn_strategy.get_connection.assert_called_once()
    mock_connection[1].execute.assert_called_once_with(query)
    mock_connection[1].fetchall.assert_called_once()
    mock_connection[0].close.assert_called_once()
    assert result == [{"id": 1, "name": "Test"}]


def test_ingest_failure_raises_error(
    mock_conn_strategy, query, mock_connection
):
    """
    Test that a DatabaseIngestionError is raised if the query fails.
    """
    mock_connection[1].execute.side_effect = Exception("Query failed")

    ingestion = PostgresIngestion(mock_conn_strategy, query)

    with pytest.raises(DatabaseIngestionError, match="Query failed"):
        ingestion.ingest()

    mock_connection[0].close.assert_called_once()
