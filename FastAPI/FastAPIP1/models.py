from pydantic import BaseModel

class ItemPayload(BaseModel):
    item_id: int
    item_name: str
    quantity: int
    description: str | None = None
    price: float