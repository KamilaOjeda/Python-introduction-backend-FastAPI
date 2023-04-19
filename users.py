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
    name: str # objeto de tipo Usuario, el nam tiene que ser String
    surname: str
    url: str
    age: int

users_list = [User(name= "Natalia", surname="Nati", url="https://nati.com", age="35"),
              User(name= "Rodrigo", surname="Rodri", url="https://rodri.com", age="25")]

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