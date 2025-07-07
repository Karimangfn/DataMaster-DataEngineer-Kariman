import os
from unittest.mock import patch

import pytest
from src.application.validators.env_vars_validator import validate_env_vars
from src.domain.exceptions.exceptions import MissingEnvironmentVariableError


@pytest.fixture
def required_env_vars():
    """
    Provides the list of required environment variables for testing.
    """
    return ["VAR1", "VAR2"]


def test_validate_env_vars_success(required_env_vars):
    """
    Test that environment variables are successfully
    validated when all required variables are present.
    """
    with patch.dict(os.environ, {"VAR1": "value1", "VAR2": "value2"}):
        result = validate_env_vars(required_env_vars)
        assert result["VAR1"] == "value1"
        assert result["VAR2"] == "value2"


def test_validate_env_vars_missing(required_env_vars):
    """
    Test that MissingEnvironmentVariableError is raised
    when a required environment variable is missing.
    """
    with patch.dict(os.environ, {"VAR1": "value1"}, clear=True):
        with pytest.raises(MissingEnvironmentVariableError) as exc:
            validate_env_vars(required_env_vars)
        assert "VAR2" in str(exc.value)
