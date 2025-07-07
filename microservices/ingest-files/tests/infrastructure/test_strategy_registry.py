from src.domain.ports.ingestion_strategy import IngestionStrategy
from src.infrastructure.config.strategy_registry import \
    FILE_INGESTION_STRATEGIES
from src.infrastructure.ingestion.ingest_files_csv import IngestFilesCSV


def test_file_ingestion_strategies_mapping():
    """
    Verify that 'csv' is a supported file ingestion strategy
    and maps to the IngestFilesCSV class implementing IngestionStrategy.
    """
    assert "csv" in FILE_INGESTION_STRATEGIES
    assert FILE_INGESTION_STRATEGIES["csv"] is IngestFilesCSV
    assert issubclass(FILE_INGESTION_STRATEGIES["csv"], IngestionStrategy)
