from pydantic import BaseModel


class User(BaseModel):  # BaseModel permite crear la entidad sin necesidad de declarar el constructor
    id: str | None = None  # El id puede ser None para permitir la creación de nuevos usuarios sin especificar un id
    name: str
    surname: str
    age: int