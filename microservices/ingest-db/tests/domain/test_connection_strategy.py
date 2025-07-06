import pytest
from src.domain.ports.connection_strategy import DatabaseConnectionStrategy


def test_cannot_instantiate_abstract_class():
    """
    Test that DatabaseConnectionStrategy cannot be instantiated directly.
    """
    with pytest.raises(TypeError):
        DatabaseConnectionStrategy()


def test_subclass_without_implementation_raises_typeerror():
    """
    Test that a subclass without get_connection implementation raises error.
    """
    class IncompleteStrategy(DatabaseConnectionStrategy):
        pass

    with pytest.raises(TypeError):
        IncompleteStrategy()


def test_subclass_with_implementation_can_be_instantiated():
    """
    Test that a subclass implementing get_connection can be instantiated.
    """
    class ConcreteStrategy(DatabaseConnectionStrategy):
        def get_connection(self):
            return "mocked-connection"

    instance = ConcreteStrategy()
    assert instance.get_connection() == "mocked-connection"
