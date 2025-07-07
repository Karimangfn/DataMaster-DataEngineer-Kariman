import pytest
from src.domain.ports.ingestion_strategy import IngestionStrategy


def test_cannot_instantiate_abstract_class():
    """
    Test that instantiating IngestionStrategy directly raises TypeError.
    """
    with pytest.raises(TypeError):
        IngestionStrategy()


def test_ingestion_strategy_subclass_can_ingest():
    """
    Test that a subclass of IngestionStrategy can implement and call ingest().
    """
    class DummyStrategy(IngestionStrategy):
        def ingest(self, source_path: str, destination_path: str) -> None:
            self.called = True
            self.src = source_path
            self.dest = destination_path

    strategy = DummyStrategy()
    strategy.ingest("source.csv", "container/path.csv")

    assert strategy.called is True
    assert strategy.src == "source.csv"
    assert strategy.dest == "container/path.csv"
