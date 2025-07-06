from unittest.mock import Mock

import pytest
from src.application.services.api_ingestion_service import APIIngestionService
from src.domain.exceptions.exceptions import APIRequestError


def test_api_ingestion_success():
    """
    Test that APIIngestionService returns the expected result
    when the strategy succeeds.
    """
    mock_strategy = Mock()
    mock_strategy.ingest.return_value = "response text"
    ingestion = APIIngestionService(mock_strategy)

    result = ingestion.ingest()

    mock_strategy.ingest.assert_called_once_with()
    assert result == "response text"


def test_api_ingestion_strategy_raises():
    """
    Test that APIIngestionService raises APIRequestError
    when the strategy fails.
    """
    mock_strategy = Mock()
    mock_strategy.ingest.side_effect = Exception("API failure")
    ingestion = APIIngestionService(mock_strategy)

    with pytest.raises(APIRequestError) as exc_info:
        ingestion.ingest()

    exc = exc_info.value
    assert exc.args[0] == "Mock"
    assert isinstance(exc.args[1], Exception)
    assert str(exc.args[1]) == "API failure"
