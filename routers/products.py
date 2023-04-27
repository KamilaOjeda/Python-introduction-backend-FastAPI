# Creamos este file para tener más de una ruta y así poder hacer el ejercicio de router.
# API rest
from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   tags=["products"], 
                   responses= {404: {"message": "No encontrado"}}) ## Puede tener cualquier otro nombre, pero "router" es más claro.
                     ## Se le puede agregar un prefijo general a la ruta, por ejemplo: products.
                     ## De esta manera, la rutas siguientes solo deberan añadir la barra "/"y lo que sigue.
                     ## Los TAGS agrupan las rutas en la documentación.
# Creamos la lista de productos
products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
# Tenemos una clase que hereda el comportamiento de BaseModel
@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]