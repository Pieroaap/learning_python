from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/products",
    responses= {404: {"message":"No encontrado"}},
    tags=["Productos"]
)

# Iniciar el servidor con uvicorn products:router --reload

# Entidad 
class Product(BaseModel):  # BaseModel permite crear la entidad sin necesidad de declarar el constructor
    id: int
    name: str
    count: int

# Creamos una lista de la entidad
product_list = [Product(id= 1,name = "Detergente", count = 24), Product(id = 2, name = "Lejia", count = 28)]

@router.get("/")
async def products():
    return product_list

# Path
@router.get("/{id}")
async def product(id:int):
    return search_product(id)

#Query
@router.get("/")
async def product(id:int):
    return search_product(id)
    
@router.post("/")
async def product(product: product):
    if type(search_product(product.id)) == product:
        return "El producto ya existe"
    else:
        product_list.routerend(product)
        return "Producto registrado"

@router.put("/")
async def product(product: product):
    updated = False
    for index, saved_product in enumerate(product_list):
        if saved_product.id == product.id:
            product_list[index] = product
            updated = True
    if(updated):
        return "Producto Actualizado"
    else:
        return "Producto no actualizado"
    
@router.delete("/")
async def product(product: product):
    deleted = False
    for index, saved_product in enumerate(product_list):
        if saved_product.id == product.id:
            del product_list[index]
            deleted = True
    if(deleted):
        return "producto Eliminado"
    else:
        return "producto no eliminado"

def search_product(id:int):
    products = filter(lambda product: product.id == id, product_list)
    try:
        return list(products)[0]
    except:
        return "No se ha encontrado el producto"