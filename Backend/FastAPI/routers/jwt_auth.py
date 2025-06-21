from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
# Configuración de JWT  
ALGOTHISM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1 # Tiempo de expiración del token en minutos
SECRET_KEY = "4k12j4k1j2i41241241j2op4i1241i2h41"

router = APIRouter(prefix="/auth_jwt", tags=["Autenticación JWT"])

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
        "password": "$2a$12$VEMCBfQO2h5UNl.GaobEBuhTnU22HCCBhvLWpCNqrxeA2LhNFJbtS" # bcrypt hash of 'entrar123'
    },
    "ancany":{
        "username": "ancany",
        "full_name": "Anthony Ronaldo Navarro Carrasco",
        "email": "anthonynavarro@gmail.com",
        "disable": False,
        "password": "$2a$12$ParXmszttYXJLzkJ.ICOge9Vy5tKhmCGAs56Jll3PcM7SrzpFMCZq"  # bcrypt hash of 'entrar321'
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    else:
        return "Usuario no encontrado"
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    else:
        return "Usuario no encontrado"
    
async def auth_user(token: str = Depends(oauth2)):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGOTHISM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = search_user(username)
    if user is None or user.disable:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado o deshabilitado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user

async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario deshabilitado"
        )
    return user

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
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

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "La contraseña no es correcta"
        )
    
    access_token_expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode(
        {"sub": user.username, "exp": access_token_expiration},
        key =SECRET_KEY,
        algorithm=ALGOTHISM)
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"}  
