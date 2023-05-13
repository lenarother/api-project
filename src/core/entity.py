from pydantic import BaseModel


class ItemResponse(BaseModel):
    item_id: int
    q: str | None
