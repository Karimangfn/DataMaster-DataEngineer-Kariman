from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType
from src.modules.schemas import get_gold_schema

def test_get_gold_schema():
    """
    Testa se a função get_gold_schema retorna um StructType com os campos
    corretos e seus respectivos tipos de dados esperados para a camada Gold.
    """
    schema = get_gold_schema()
    assert isinstance(schema, StructType)

    expected_fields = [
        ("store_location", StringType),
        ("purchase_month", StringType),
        ("total_purchases", IntegerType),
        ("total_revenue", DoubleType),
        ("average_purchase_value", DoubleType),
        ("high_value_purchases", IntegerType)
    ]

    for idx, (name, dtype) in enumerate(expected_fields):
        field = schema.fields[idx]
        assert field.name == name
        assert isinstance(field.dataType, dtype)