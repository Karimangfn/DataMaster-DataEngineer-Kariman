from src.infrastructure.config import strategy_registry
from src.infrastructure.connection.postgres_connection import \
    PostgresConnection
from src.infrastructure.ingestion.postgres_ingestion import PostgresIngestion


def test_connection_strategies_contains_postgres():
    """
    Test that CONNECTION_STRATEGIES contains the expected Postgres strategy.
    """
    assert "postgresql" in strategy_registry.CONNECTION_STRATEGIES
    assert (
        strategy_registry.CONNECTION_STRATEGIES["postgresql"]
        is PostgresConnection
    )


def test_ingestion_strategies_contains_postgres():
    """
    Test that INGESTION_STRATEGIES contains the expected Postgres strategy.
    """
    assert "postgresql" in strategy_registry.INGESTION_STRATEGIES
    assert (
        strategy_registry.INGESTION_STRATEGIES["postgresql"] is PostgresIngestion
    )
