# main.py
import logging
from src.api_ingestion import APIIngestion
from src.utils import get_params_from_config  # Caso você precise de algum arquivo de configuração

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Função principal que faz a ingestão de dados de diferentes fontes.
    """
    try:
        # Você pode pegar os parâmetros do arquivo de configuração, ou de variáveis de ambiente
        config = get_params_from_config()  # Retorna os parâmetros necessários para a ingestão

        for api_config in config["apis"]:
            api_url = api_config["url"]
            api_type = api_config["type"]  # Tipo da API (ex: REST ou GraphQL)
            params = api_config["params"]

            # Criação do objeto de ingestão de dados
            ingestion_service = APIIngestion(api_url, api_type)

            # Realizar a ingestão
            data = ingestion_service.ingest(params)

            # Log de sucesso
            logger.info(f"Ingestão realizada com sucesso para API: {api_url}")

            # Você pode armazenar ou fazer algo com os dados depois da ingestão

    except Exception as e:
        logger.error(f"Erro durante a ingestão de dados: {str(e)}")


if __name__ == "__main__":
    main()