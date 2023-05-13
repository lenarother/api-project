from .entity import ItemResponse

docs = [
    {"item_id": 1, "q": "Foo"},
    {"item_id": 2, "q": "Bar"},
    {"item_id": 3, "q": "Bazz"},
    {"item_id": 3},
]

def get_item(item_id: int) -> ItemResponse:
    """Finds item with item_id"""
    for d in docs:
        if d["item_id"] == item_id:
            return d
    raise IndexError(f"No item with id {item_id}")
