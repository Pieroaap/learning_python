from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

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
        "disable": False,
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
        return UserDB(users_db[username])
    else:
        return "Usuario no encontrado"
    
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username) 
    if not user_db:
        raise HTTPException(
            status_code=400, 
            detail="El usuario no es correcto"
            )
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=400,
            detail= "La contraseña no es correcta"
        )
    