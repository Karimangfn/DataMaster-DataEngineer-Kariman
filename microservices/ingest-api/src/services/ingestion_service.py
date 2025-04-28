from src.ingestion.api_ingestor import APIIngestor


class IngestionService:
    """Gerenciador de ingestão de dados via API"""

    def __init__(self, config: dict):
        # Configuração que define o tipo de ingestor (API)
        self.api_ingestor = APIIngestor(config["api_url"], config["api_key"])

    def execute(self):
        """Executa o processo de ingestão de dados via API"""
        return self.api_ingestor.fetch_data()
