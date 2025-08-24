from src.modules.schemas import get_customer_schema


def test_get_customer_schema_fields():
    """
    Test that get_customer_schema returns a schema with the expected fields
    and the correct number of columns.
    """
    schema = get_customer_schema()
    field_names = [f.name for f in schema.fields]
    expected = [
        "customer_id", "first_name", "last_name", "email",
        "purchase_date", "total_amount", "product",
        "store_location", "cpf", "credit_card_number"
    ]
    assert field_names == expected
    assert len(schema.fields) == 10
