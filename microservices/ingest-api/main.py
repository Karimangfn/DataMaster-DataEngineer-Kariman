import logging
import json
from src.strategy.ingestion_api import APIIngestion
from src.utils.utils import load_config, convert_to_json

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    """
    Função principal que faz a ingestão de dados da API.
    """
    try:
        config = load_config("config.yaml")

        api_url = config["api"]["url"]
        api_key = config["api"]["key"]
        
        ingestion_service = APIIngestion(api_url, "rest")

        params = {"key": api_key}

        response = ingestion_service.ingest(params)

        data = convert_to_json(response)

        print(data)

        logger.info(f"Ingestão realizada com sucesso para API: {api_url}")

    except Exception as e:
        logger.exception(f"Erro crítico durante a execução: {e}")

if __name__ == "__main__":
    main()
