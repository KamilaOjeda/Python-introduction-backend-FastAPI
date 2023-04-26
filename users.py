from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciar el server: uvicorn users:app --reload
"""
@app.get("/users")
async def users():
    return "¡Hola, Users!"
"""

# Entidad user

class User(BaseModel): # Base Model nos da la capacidad de crear una entidad.
    id: int
    name: str # objeto de tipo Usuario, el nam tiene que ser String
    surname: str
    url: str
    age: int

# Base de datos inventada:
users_list = [User(id= 1, name= "Natalia", surname="Nati", url="https://nati.com", age=35),
              User(id= 2, name= "Rodrigo", surname="Rodri", url="https://rodri.com", age=25)]

## Operación GET, para leer datos.

@app.get("/usersjson")
async def usersjson():
    return [{"id": 1, "name": "Natalia", "surname": "Nati", "url": "https://nati.com", "age": 35},
            {"id": 2, "name": "Rodrigo", "surname": "Rodri", "url": "https://rodri.com", "age": 25},
            {"id": 3, "name": "Patricia", "surname": "Paty", "url": "https://paty.com", "age": 19}]
 
# Definimos lista users, imaginamos que está en una base de datos.    
# users = [User("Luciana", "Luci", "https://luci.com", "35")]

# Tenemos una clase que hereda el comportamiento de BaseModel
@app.get("/users")
async def users():
    return users_list

# Tenemos una clase que hereda el comportamiento de BaseModel
# Le damos un nombre relacionado con la opración que va a realizar
# Le pasamos un parámetro, en este caso será el id

# Path
@app.get("/user/{id}") # El path /user/{id} tiene un path parameter "id" que debería ser un int.
async def users(id: int): # Le pasamos el parámetro tipado, en este caso es si o si un entero: int.
    return search_user(id)

    
# Limitamos y aseguramos que las peticiones sean las correctas.

# Query
@app.get("/userquery") # El path /user/{id} tiene un path parameter "id" que debería ser un int. Por otro lado, /userquery tmabién podría llamarse solo /user.
async def users(id: int): # Le pasamos el parámetro tipado, en este caso es si o si un entero: int.
    return search_user(id)
    
## Operación POST: Agregar
### Para que cualquier operación esté expuesta en la API: @app + el tipo de operación, es suficiente.
@app.post("/user/") 
    # Implementamos la operación:
async def user(user: User): ## Le pasamos lo que queremos agregar, en este caso sería una entidad User.
    if type(search_user(user.id)) == User: ## Verificamos si el usuario ya existe en la lista.
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user) ## append: Agrega elementos a una lista.
        ## Buena práctica, si de verdad se ha agregado, retorno el usuario.
        return user
## Operación PUT: Actualiza
### Actualizar el usuario completo.
### Se puede actualizar los parámetros por separado, para esto debe utilizar PATCH.
@app.put("/user/")
async def user(user: User): ## Le pasamos el usuario que queremos actualizar.
    found = False # Una variable para controlar si he llegado al usuario o no,
    # Recorremos la lista y si encontramos un usuarioio que coincida con el que queremos actualizar, pues se actualiza.
    for index, saved_user in enumerate(users_list): ## Enumerate, es una clase de Python para enumerar los elementos de la lista.
        if saved_user.id == user.id: # Si lo encontramos, accedemos a él.
            users_list[index] = user # Acceder al que hemos encontrado.
            found = True # Una variable para controlar si he llegado al usuario o no,
    if not found:
        return {"error": "No se ha actualizado el Usuario"} # Se puede mejorar el manejo de errores.
    ## Buena práctica, si de verdad se ha actualizado, retorno el usuario.
    else:
        return user

@app.delete("/user/{id}") ## Utilizamos query, porque el ID es obligatorio.
async def user(id: int): ## Le pasamos el ID del usuario que queremos eliminar.
    found = False # Una variable para controlar si he llegado al usuario o no,
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True # Una variable para controlar si he llegado al usuario o no,
    if not found:
        return {"error": "No se ha eliminado el usuario"}
    
# Función para buscar el usuario por id.
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) # Filter: función pre cargada en python y es una función superior
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el Usuario"}
