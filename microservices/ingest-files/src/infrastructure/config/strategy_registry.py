from typing import Dict, Type
from src.domain.ports.ingest_strategy import IngestionStrategy
from src.infrastructure.ingestion.ingest_files_csv import IngestFilesCSV

# Mapeamento das estratégias de ingestão de arquivos suportadas, pelo tipo/extensão
FILE_INGESTION_STRATEGIES: Dict[str, Type[IngestionStrategy]] = {
    "csv": IngestFilesCSV
}
