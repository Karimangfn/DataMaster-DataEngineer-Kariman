from unittest.mock import Mock, patch

import pytest
from src.application.services.database_ingestion_service import \
    DatabaseIngestionService
from src.domain.exceptions.exceptions import DatabaseIngestionError


@pytest.fixture
def mock_success_strategy():
    """
    Fixture for a strategy mock that simulates successful ingestion.
    """
    mock = Mock()
    mock.ingest.return_value = "mocked_data"
    return mock


@pytest.fixture
def mock_failing_strategy():
    """
    Fixture for a strategy mock that simulates a failure.
    """
    mock = Mock()
    mock.ingest.side_effect = RuntimeError("Simulated failure")
    return mock


@pytest.fixture
def ingestion_service_success(mock_success_strategy):
    """
    Fixture for a service using a successful strategy.
    """
    return DatabaseIngestionService(strategy=mock_success_strategy)


@pytest.fixture
def ingestion_service_failure(mock_failing_strategy):
    """
    Fixture for a service using a failing strategy.
    """
    return DatabaseIngestionService(strategy=mock_failing_strategy)


def test_ingest_returns_data_on_success(ingestion_service_success):
    """
    Test that ingest returns data when strategy succeeds.
    """
    result = ingestion_service_success.ingest()
    assert result == "mocked_data"


def test_ingest_raises_custom_error_on_failure(ingestion_service_failure):
    """
    Test that a DatabaseIngestionError is raised when strategy fails.
    """
    with pytest.raises(DatabaseIngestionError) as exc_info:
        ingestion_service_failure.ingest()
    assert "Ingestion failed using strategy" in str(exc_info.value)


@patch("src.application.services.database_ingestion_service.logger")
def test_logs_info_on_success(mock_logger, ingestion_service_success):
    """
    Test that logger.info is called on successful ingestion.
    """
    ingestion_service_success.ingest()
    assert mock_logger.info.called
    assert any(
        "completed successfully" in call.args[0]
        for call in mock_logger.info.call_args_list
    )


@patch("src.application.services.database_ingestion_service.logger")
def test_logs_error_on_failure(mock_logger, ingestion_service_failure):
    """
    Test that logger.error is called on ingestion failure.
    """
    with pytest.raises(DatabaseIngestionError):
        ingestion_service_failure.ingest()
    assert mock_logger.error.called
    assert any(
        "Failed to ingest using strategy" in call.args[0]
        for call in mock_logger.error.call_args_list
    )
