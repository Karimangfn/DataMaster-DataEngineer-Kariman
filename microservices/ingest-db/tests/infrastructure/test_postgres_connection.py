from unittest.mock import MagicMock, patch

import pytest
from psycopg2 import OperationalError
from src.infrastructure.connection.postgres_connection import \
    PostgresConnection


@pytest.fixture
def valid_connection_string():
    """Fixture that provides a valid PostgreSQL connection string."""
    return "dbname=test user=test password=test host=localhost"


@patch("src.infrastructure.connection.postgres_connection.psycopg2.connect")
def test_get_connection_success(mock_connect, valid_connection_string):
    """
    Test that a PostgreSQL connection is successfully
    returned when credentials are valid.
    """
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    pg_conn = PostgresConnection(valid_connection_string)
    conn = pg_conn.get_connection()

    mock_connect.assert_called_once_with(
        valid_connection_string,
        cursor_factory=mock_connect.call_args.kwargs.get("cursor_factory")
    )
    assert conn == mock_conn


@patch("src.infrastructure.connection.postgres_connection.psycopg2.connect")
def test_get_connection_failure(mock_connect, valid_connection_string):
    """
    Test that an exception is raised and logged when
    the PostgreSQL connection fails.
    """
    mock_connect.side_effect = OperationalError("Connection failed")

    pg_conn = PostgresConnection(valid_connection_string)

    with pytest.raises(OperationalError, match="Connection failed"):
        pg_conn.get_connection()

    mock_connect.assert_called_once()
