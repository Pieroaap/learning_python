from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    responses= {404: {"message":"No encontrado"}},
    tags=["Usuarios"]
)

# Iniciar el servidor con uvicorn users:router --reload

# Entidad 
class User(BaseModel):  # BaseModel permite crear la entidad sin necesidad de declarar el constructor
    id: int
    name: str
    surname: str
    age: int

# Creamos una lista de la entidad
user_list = [User(id= 1,name = "Piero", surname = "Alvarado", age = 24), User(id = 2, name = "Jhoan", surname = "Ramos", age = 28)]

@router.get("/")
async def users():
    return user_list

# Path
@router.get("/{id}")
async def user(id:int):
    return search_user(id)

#Query
@router.get("/")
async def user(id:int):
    return search_user(id)
    
@router.post("/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return "El usuario ya existe"
    else:
        user_list.routerend(user)
        return "Usuario registrado"

@router.put("/")
async def user(user: User):
    updated = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            updated = True
    if(updated):
        return "Usuario Actualizado"
    else:
        return "Usuario no actualizado"
    
@router.delete("/")
async def user(user: User):
    deleted = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            del user_list[index]
            deleted = True
    if(deleted):
        return "Usuario Eliminado"
    else:
        return "Usuario no eliminado"

def search_user(id:int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return "No se ha encontrado el usuario"