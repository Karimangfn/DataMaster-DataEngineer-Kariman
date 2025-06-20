from unittest.mock import MagicMock, patch

import pytest
from src.domain.ports.authentication_strategy import AuthenticationStrategy
from src.infrastructure.ingestion.rest_api_ingestion import RestAPIIngestion


@pytest.fixture
def mock_auth_strategy():
    """
    Fixture that provides a mock authentication strategy.
    """
    mock_auth = MagicMock(spec=AuthenticationStrategy)
    mock_auth.get_query_params.return_value = {"q": "test"}
    mock_auth.get_headers.return_value = {"Auth": "token"}
    return mock_auth


@pytest.fixture
def rest_api(mock_auth_strategy):
    """
    Fixture that provides an instance of RestAPIIngestion with
    a URL and mock authentication strategy.
    """
    return RestAPIIngestion("http://fakeapi.com/data", mock_auth_strategy)


@patch("src.infrastructure.ingestion.rest_api_ingestion.requests.get")
def test_rest_api_ingestion_success(mock_get, rest_api):
    """
    Test that ingest returns response text when the API call succeeds.
    """
    mock_response = MagicMock()
    mock_response.text = '{"data": 123}'
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = rest_api.ingest()

    mock_get.assert_called_once_with(
        "http://fakeapi.com/data",
        params={"q": "test"},
        headers={"Auth": "token"},
        verify=False,
    )
    assert result == '{"data": 123}'


@patch("src.infrastructure.ingestion.rest_api_ingestion.requests.get")
def test_rest_api_ingestion_failure(mock_get, rest_api):
    """
    Test that ingest raises APIIngestionError when the request fails.
    """
    mock_get.side_effect = Exception("Connection error")

    with pytest.raises(Exception) as exc:
        rest_api.ingest()

    assert "Connection error" in str(exc.value)
