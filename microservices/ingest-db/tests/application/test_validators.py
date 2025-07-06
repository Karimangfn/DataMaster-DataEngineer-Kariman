import os
from unittest.mock import patch

import pytest
from src.application.validators.env_vars_validator import validate_env_vars
from src.domain.exceptions.exceptions import MissingEnvironmentVariableError


@pytest.fixture
def required_vars():
    """
    Fixture for a list of required environment variable names.
    """
    return ["VAR_A", "VAR_B", "VAR_C"]


@patch.dict(os.environ, {
    "VAR_A": "value_a", "VAR_B": "value_b", "VAR_C": "value_c"
    }
)
def test_validate_env_vars_returns_values(required_vars):
    """
    Test that validate_env_vars returns correct values
    when all variables are set.
    """
    result = validate_env_vars(required_vars)
    assert result == {
        "VAR_A": "value_a",
        "VAR_B": "value_b",
        "VAR_C": "value_c"
    }


@patch.dict(os.environ, {}, clear=True)
def test_validate_env_vars_raises_if_missing(required_vars):
    """
    Test that MissingEnvironmentVariableError is raised
    when required variables are missing.
    """
    with pytest.raises(MissingEnvironmentVariableError) as exc_info:
        validate_env_vars(required_vars)
    assert set(exc_info.value.args[0]) == set(required_vars)


@patch.dict(os.environ, {
    "VAR_A": "value_a", "VAR_B": "", "VAR_C": "value_c"
    }
)
def test_validate_env_vars_raises_if_empty_var(required_vars):
    """
    Test that empty environment variables also
    trigger the MissingEnvironmentVariableError.
    """
    with pytest.raises(MissingEnvironmentVariableError) as exc_info:
        validate_env_vars(required_vars)
    assert "VAR_B" in exc_info.value.args[0]
