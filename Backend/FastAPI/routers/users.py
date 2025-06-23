from fastapi import APIRouter, status, HTTPException
from db.client import db_client
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(
    prefix="/users",
    responses= {404: {"message":"No encontrado"}},
    tags=["Usuarios"]
)

# Iniciar el servidor con uvicorn users:router --reload

# Creamos una lista de la entidad
user_list = []

@router.get("/", response_model=list[User])  # Usa response_model, no response_class
async def get_users():
    users = list(db_client.users.find())
    return users_schema(users)

# Path
@router.get("/{id}") 
async def user(id:str):
    return search_user("_id", ObjectId(id))  # Convertir el id a ObjectId para buscar en la base de datos
    
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED) #Añadir un usuario
async def user(user: User):
    if type(search_user_by_name(user.name)) == User:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe"
        )
    else:
    #Convertir el objeto User a un diccionario
        user_dict = dict(user) 
        #Eliminar el id para que la base de datos lo genere automáticamente
        del user_dict["id"] 
        # Insertar el usuario en la base de datos 
        id = db_client.users.insert_one(user_dict).inserted_id

        new_user = user_schema(db_client.users.find_one({"_id": id})) #Buscar el usuario por su id      
    # Añadir el id al objeto User
        return User(**new_user)  # Convertir el ObjectId a str para que sea compatible con Pydantic


@router.put("/") #Actualizar un usuario
async def user(user: User):
    user_dict = dict(user)  # Convertir el objeto User a un diccionario
    del user_dict["id"]  # Eliminar el id para que la base de datos lo actualice correctamente
    try:
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no actualizado o no encontrado"
        )
    return search_user("_id", ObjectId(user.id))  # Buscar el usuario por su id y devolverlo
    
@router.delete("/{id}") #Eliminar un usuario
async def user(id:str, status_code=status.HTTP_204_NO_CONTENT):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

def search_user(field:str, key): 
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error":"No se ha encontrado el usuario con ese id"}
    
def search_user_by_name(name:str): 
    try:
        return User(**db_client.users.find_one({"name": name}))
    except:
        return {"error":"No se ha encontrado el usuario con ese nombre"}
    
