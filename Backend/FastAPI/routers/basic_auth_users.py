from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth_basic", tags=["Autenticación Básica"])

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):  # BaseModel permite crear la entidad sin necesidad de declarar el constructor
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB(User):
    password: str

users_db = {
    "pialpa":{
        "username": "pialpa",
        "full_name": "Piero Alexis Alvarado Palomino",
        "email": "pieroalexis33@gmail.com",
        "disable": True,
        "password": "entrar123"
    },
    "ancany":{
        "username": "ancany",
        "full_name": "Anthony Ronaldo Navarro Carrasco",
        "email": "anthonynavarro@gmail.com",
        "disable": False,
        "password": "entrar321"
    }
}

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    else:
        return "Usuario no encontrado"
    
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    else:
        return "Usuario no encontrado"

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no válidas",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario deshabilitado"
        )
    return user
    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username) 
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="El usuario no es correcto"
            )
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "La contraseña no es correcta"
        )
    return {
        "access_token": user.username, 
        "token_type": "bearer"}
    
    
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
    
@router.get("/")
async def root():
    return "Servicio levantado con normalidad"