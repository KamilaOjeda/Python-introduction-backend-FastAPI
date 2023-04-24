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

users_list = [User(id= 1, name= "Natalia", surname="Nati", url="https://nati.com", age="35"),
              User(id= 2, name= "Rodrigo", surname="Rodri", url="https://rodri.com", age="25")]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Natalia", "surname": "Nati", "url": "https://nati.com", "age": "35"},
            {"name": "Rodrigo", "surname": "Rodri", "url": "https://rodri.com", "age": "25"},
            {"name": "Patricia", "surname": "Paty", "url": "https://paty.com", "age": "19"}]
 
# Definimos lista users, imaginamos que está en una base de datos.    
# users = [User("Luciana", "Luci", "https://luci.com", "35")]

# Tenemos una clase que hereda el comportamiento de BaseModel
@app.get("/users")
async def users():
    return users_list

# Tenemos una clase que hereda el comportamiento de BaseModel
# Le damos un nombre relacionado con la opración que va a realizar
# Le pasamos un parámetro, en este caso será el id
@app.get("/user/{id}") # El path /user/{id} tiene un path parameter "id" que debería ser un int.
async def users(id: int): # Le pasamos el parámetro tipado, en este caso es si o si un entero: int.
    users = filter(lambda user: user.id == id, users_list) # Filter: función pre cargada en python y es una función superior
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el Usuario"}