# Autorización OAUTH2
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel ## Par que el objeto que tenemos más abajo definido como una clase, se pueda pasar a través de la red de una manera más sencilla, se pueda transformar en JSON y así.
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm ## Clases que se encargan de autenticar y la otra la forma en la que se enviará desde el cliente los datos y la forma en la que el backennd autenticará los datos en el sistema, es decir los capturará, respectivamente.

app = FastAPI()

# Creamos una instancia de nuestro sistema de autenticación
oauht2 = OAuth2PasswordBearer(tokenUrl="login")

# Entidad User que irá a través de la red / Tmb es un objeto, el obj User
class User(BaseModel): # Base Model nos da la capacidad de crear una entidad.
    username: str
    full_name: str # objeto de tipo Usuario, el nam tiene que ser String
    email: str
    disabled: bool

# Entidad UserDB para representar al Usuario de Base de Datos.
class UserDB(User): # Tiene los mismo datos que el User creado más arriba, además incluye password.
    password: str

# Base de Datos de usuarios   
users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "123456" ## La contraseña debería estar encriptada.
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "password": "654321" ## La contraseña debería estar encriptada.
    },
}

# Definimos una función search_user para buscar algún usuario en la base de datos.
def search_user(username: str):
    if username in users_db: ## Si el username ingresado está en la base de datos, entonces,
        return UserDB(**users_db[username]) ## Para hacer este llamado será necesario anteponer los "**", para indicarle que pueden ir varios.

# Definimos un criterio de dependencia
async def current_user(token: str = Depends(oauht2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticación inválidas",
            headers={"www-Authenticate": "Bearer"})


# Implementamos la operación de autenticación, con usuario y contraseña
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()): ## Significa que una operación va a recibir datos, pero no depende de nadie.
    user_db = users_db.get(form.username) ## Ir a la base de datos users_db y con el GET buscarmos si de verdad está ese usuario.
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    ## Comprobar si de  verdad la contraseña que nos ha llegado coincide con la de la base de datos.
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"} ## Bearer es un standard

# Implementamos esta operación para que nos diga cuando estamos autenticados.
@app.get("/users/me")
async def me(user: User = Depends(current_user)): ## Esta operación depende de que el usuario esté autenticado, por eso utilizamos Depends
    return user