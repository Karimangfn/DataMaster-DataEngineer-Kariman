from typing import Any, Dict, Optional

import pytest
from src.domain.ports.ingestion_strategy import APIIngestionStrategy


@pytest.fixture
def dummy_strategy():
    """
    Fixture that provides a dummy implementation of APIIngestionStrategy
    for testing purposes.
    """
    class DummyStrategy(APIIngestionStrategy):
        def ingest(
            self,
            data_source: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, Any]] = None
        ) -> Any:
            return {
                "data_source": data_source,
                "params": params,
                "headers": headers
            }
    return DummyStrategy()


def test_api_ingestion_strategy_is_abstract():
    """
    Test that APIIngestionStrategy cannot be instantiated directly,
    enforcing its abstract behavior.
    """
    with pytest.raises(TypeError):
        APIIngestionStrategy()


def test_dummy_strategy_ingest(dummy_strategy):
    """
    Test that the dummy ingestion strategy returns the correct structure
    with the given data source, params, and headers.
    """
    result = dummy_strategy.ingest(
        data_source="http://api.example.com/data",
        params={"key": "value"},
        headers={"Authorization": "Bearer token"}
    )
    assert result["data_source"] == "http://api.example.com/data"
    assert result["params"] == {"key": "value"}
    assert result["headers"] == {"Authorization": "Bearer token"}
