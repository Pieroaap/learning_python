from fastapi import FastAPI
from routers import basic_auth_users, jwt_auth, products, users  # Para obtener las rutas de los modulos products y users
from fastapi.staticfiles import StaticFiles # Para obtener recursos estáticos

app = FastAPI()

# Routes
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth.router)  # Asegúrate de importar jwt_auth 
app.include_router(basic_auth_users.router)  # Asegúrate de importar basic_auth_users

# Estáticos
app.mount("/static",StaticFiles(directory="static"), name = "statico")

@app.get("/")
async def root():
    return "Servicio levantado con normalidad"

@app.get("/url")
async def url():
    return {"url":"www.google.com"}