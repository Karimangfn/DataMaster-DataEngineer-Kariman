from src.infrastructure.authentication.query_param_auth import \
    APIKeyQueryParamAuth
from src.infrastructure.ingestion.rest_api_ingestion import RestAPIIngestion

INGESTION_STRATEGIES = {
    "rest": RestAPIIngestion
}

AUTH_STRATEGIES = {
    "query_param": APIKeyQueryParamAuth
}
