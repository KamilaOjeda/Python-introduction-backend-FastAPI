from fastapi import FastAPI # Importamos fastAPI
from routers import products, users # Importamos el fichero de products y users DESDE LA CARPETA ROUTERS, que es donde están ubicados.
from fastapi.staticfiles import StaticFiles # Importamos la clase para poder manipular los recursos estáticos.
app = FastAPI() #Creamos un objeto app, por convención, que instancie la clase FastAPI()

# ROUTERS
## Accedemos a la instancia app y operacion: include_router
app.include_router(products.router)
app.include_router(users.router)

# RECURSOS ESTÁTICOS
## Para exponer un recurso estático
app.mount("/static", StaticFiles(directory="static"), name="static")
## http://127.0.0.1:8000/static/images/backend.png

# Creamos una función que se llame root
# Con @app ya estamos accediendo al contexto de fastAPI
# Siempre que llamamos a un servidor, la operación tiene que ser asíncrona: async
# - En nuestro caso, este decorador le dice a FastAPI que la función que está debajo, corrsponde al path "/" con una operación GET.

# Url local: http://127.0.0.1:8000

@app.get("/") # La raíz de la IP donde se está despegango la web
async def root():
    return "¡Hola, FastAPI!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"} # Estandar absoluto para consumir API, 95% de APIs trabaja con JSON. Esto nos devuleve un JSON.