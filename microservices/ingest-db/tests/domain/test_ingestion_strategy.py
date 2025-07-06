import pytest
from src.domain.ports.ingestion_strategy import DatabaseIngestionStrategy


def test_cannot_instantiate_abstract_class():
    """
    Test that DatabaseIngestionStrategy cannot be instantiated directly.
    """
    with pytest.raises(TypeError):
        DatabaseIngestionStrategy()


def test_subclass_without_implementation_raises_typeerror():
    """
    Test that a subclass without ingest implementation raises an error.
    """
    class IncompleteStrategy(DatabaseIngestionStrategy):
        pass

    with pytest.raises(TypeError):
        IncompleteStrategy()


def test_subclass_with_implementation_can_be_instantiated():
    """
    Test that a subclass implementing ingest can be instantiated and works.
    """
    class ConcreteStrategy(DatabaseIngestionStrategy):
        def ingest(self):
            return "mocked-ingestion-result"

    strategy = ConcreteStrategy()
    assert strategy.ingest() == "mocked-ingestion-result"
