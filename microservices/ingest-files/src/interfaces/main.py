import logging

from src.services.ingestion_service import IngestionService
from src.utils.utils import load_config

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    """
    Função principal para mover arquivos.
    """
    try:
        # Carregar configurações
        config = load_config("config.yaml")

        # Inicializa o serviço de ingestão com as configurações carregadas
        ingest_service = IngestionService(config)

        # Executa o processo de ingestão
        ingest_service.execute()

        logger.info("Ingestão de arquivos realizada com sucesso!")

    except Exception as e:
        logger.exception(f"Erro crítico durante a execução: {e}")

if __name__ == "__main__":
    main()