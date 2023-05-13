import pytest
from src.core.boundery import get_item


def test_get_item():
    assert get_item(1) == {"item_id": 1, "q": "Foo"}


def test_get_item_raises_when_no_item():
    with pytest.raises(IndexError):
        get_item(999)
