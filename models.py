from sqlalchemy.types import Integer, VARCHAR, TIMESTAMP
from pydantic import BaseModel

class bicycles(BaseModel):
    id: int
    name: str | None = None
    price: str | None = None
    stock: str | None = None