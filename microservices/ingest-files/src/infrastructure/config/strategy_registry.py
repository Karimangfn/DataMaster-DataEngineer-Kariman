from typing import Dict, Type

from src.domain.ports.ingestion_strategy import IngestionStrategy
from src.infrastructure.ingestion.ingest_files_csv import IngestFilesCSV

#: Mapping of supported file ingestion strategies by file extension.
FILE_INGESTION_STRATEGIES: Dict[str, Type[IngestionStrategy]] = {
    "csv": IngestFilesCSV,
}
