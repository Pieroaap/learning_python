from pydantic import BaseModel

class Product(BaseModel):  # BaseModel permite crear la entidad sin necesidad de declarar el constructor
    id: int
    name: str
    count: int