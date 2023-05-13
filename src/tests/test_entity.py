from src.core.entity import ItemResponse


def test_item_response():
    assert ItemResponse(item_id=1)
    assert ItemResponse(item_id=1, q="Foo")
