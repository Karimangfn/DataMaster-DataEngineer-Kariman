from .ingestion_strategy import IngestionStrategy

class RestAPIIngestion(IngestionStrategy):
    def ingest(self, data_source):
        # Lógica para ingestão via API
        return f"Ingesting data from API: {data_source}"
