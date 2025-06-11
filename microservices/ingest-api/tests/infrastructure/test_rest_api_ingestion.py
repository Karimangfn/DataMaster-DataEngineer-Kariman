from unittest.mock import MagicMock, patch

import pytest
from src.infrastructure.ingestion.rest_api_ingestion import RestAPIIngestion


@pytest.fixture
def rest_api():
    """
    Fixture that provides an instance of RestAPIIngestion for testing.
    """
    return RestAPIIngestion()


@patch("src.infrastructure.ingestion.rest_api_ingestion.requests.get")
def test_rest_api_ingestion_success(mock_get, rest_api):
    """
    Test that the `ingest` method returns the expected response
    text when the API call is successful.
    """
    mock_response = MagicMock()
    mock_response.text = '{"data": 123}'
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = rest_api.ingest(
        "http://fakeapi.com/data",
        params={"q": "test"},
        headers={"Auth": "token"}
    )

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
    Test that the `ingest` method raises Exception when the request fails.
    """
    mock_get.side_effect = Exception("Connection error")

    with pytest.raises(Exception) as exc:
        rest_api.ingest("http://fakeapi.com/data")

    assert "Connection error" in str(exc.value)
