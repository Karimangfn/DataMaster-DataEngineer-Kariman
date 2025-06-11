from unittest.mock import Mock

import pytest
from src.application.services.api_ingestion_service import APIIngestion
from src.domain.exceptions.exceptions import APIRequestError


def test_api_ingestion_success():
    mock_strategy = Mock()
    mock_strategy.ingest.return_value = "response text"
    ingestion = APIIngestion("http://fake-api.com", mock_strategy)

    result = ingestion.ingest(params={"foo": "bar"})
    mock_strategy.ingest.assert_called_once_with(
        "http://fake-api.com",
        {"foo": "bar"}
    )
    assert result == "response text"


def test_api_ingestion_strategy_raises():
    mock_strategy = Mock()
    mock_strategy.ingest.side_effect = Exception("API failure")
    ingestion = APIIngestion("http://fake-api.com", mock_strategy)

    with pytest.raises(APIRequestError):
        ingestion.ingest()
