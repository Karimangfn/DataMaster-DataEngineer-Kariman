from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType
from src.modules.schemas import get_gold_schema

def test_get_gold_schema():
    """
    Tests if the function get_gold_schema returns a StructType with the correct
    fields and their expected data types for the Gold layer.
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