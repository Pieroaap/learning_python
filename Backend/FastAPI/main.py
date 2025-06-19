from fastapi import FastAPI
from routers import products, users  # Para obtener las rutas de los modulos products y users
from fastapi.staticfiles import StaticFiles # Para obtener recursos estáticos

app = FastAPI()

# Routes
app.include_router(products.router)
app.include_router(users.router)

# Estáticos
app.mount("/static",StaticFiles(directory="static"), name = "statico")

@app.get("/")
async def root():
    return "Servicio levantado con normalidad"

@app.get("/url")
async def url():
    return {"url":"www.google.com"}