# Python-introduction-backend-FastAPI
Curso introductorio de Python para backend.

# Fast API
El tipado ayuda a fastAPI a validar los datos. Y Python es de tipado dinámico, por eso se puede utilizar con fastAPI.

Para activar el entoro virtual de Python: source fastapiback-env/bin/activate
Permite trabajar en un servidor en local -> "uvicorn"
 - Para iniciar el server: uvicorn main:app --reload
## pip
Se necesita un empaquetador, en nuestro caso es pip3

## root
No se debería llamar a todo root

## Peticiones HTTP
INFO:     127.0.0.1:52131 - "GET /url HTTP/1.1" 200 OK
INFO:     127.0.0.1:52132 - "GET /km HTTP/1.1" 404 Not Found

## Documentación

Donde se cuenta todas las peticiones que tiene la API, que hace cada petición
Qué rutas existen y qué devuelven.

Se puede ver en la web con: 
- Swagger: http://127.0.0.1:8000/docs (el más utilizado)
- Redocly: http://127.0.0.1:8000/redoc

## Operación GET
### Opciones:
- Postman: Herramienta para poder ejecutar operaciones a un API (interactuar con el backend). Captura todo con lo que esté relacionado una petición.

- Thunder Client: Extensión para VSCode, muy similar a Postman.

## Operaciones

Operación se refiere a uno de los "métodos" de HTTP, que serían las peticiones HTTP. Con el protocolo HTTP te puedes comunicar con cada "path" usando uno o más de estos métodos, y normalmente se utilizar para realizar una acción específica.

- POST: para crear datos
- GET: para leer datos
- PUT: para actualizae datos
- DELETE: para borrar datos

Y otros exóticos:

- OPTIONS
- HEAD
- PATCH
- TRACE

# Creación API

Un API para usuarios generales.

## CRUD: 
- Create, Read, Update, Delete (operaciones básica para implementar un API)

## DECORADOR: 
- @decorador, la sintaxis @algo se llama "decorador" en Python.
- Se pone encima de una función. Es como un lindo sombrero decorado.
- Un "@decorador" toma la función que tiene inmediatamente debajo y hace algo con ella.
