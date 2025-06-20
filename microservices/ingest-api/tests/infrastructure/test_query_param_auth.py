from src.infrastructure.authentication.query_param_auth import \
    APIKeyQueryParamAuth


def test_get_query_params_returns_api_key():
    """
    Test that get_query_params returns the correct API key in a dictionary.
    """
    auth = APIKeyQueryParamAuth("my-api-key")
    assert auth.get_query_params() == {"key": "my-api-key"}


def test_get_headers_returns_empty_dict():
    """
    Test that get_headers returns an empty dictionary.
    """
    auth = APIKeyQueryParamAuth("any-key")
    assert auth.get_headers() == {}
