from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid

app = FastAPI()

posts = [

]


class User(BaseModel):
    id_usuario: int
    nombre_usuario: str
    apellido_usuario: str
    edad: int


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
def obtener_usuarios():
    return posts


@app.post("/posts")
def guardar_usuario(post: User):
    post.id_usuario = str(uuid())  # esto le dara un id aleatorio y unico
    posts.append(post.dict())
    return posts[-1]  # me devolverá la última entrada o post.


@app.get("/posts/{post_id_usuario}")  # obtener el post mediante un id
def obtener_post(post_id_usuario: str):
    print(post_id_usuario)
    for post in posts:
        if post["id_usuario"] == post_id_usuario:
            return post
    raise HTTPException(status_code=404,
                        detail="post not found")  # usa http exepciton para dar una explicacion de error


@app.delete("/posts/{post_id_usuario}")
def borrar_post(post_id_usuario: str):
    for i, post in enumerate(posts):
        if post["id_usuario"] == post_id_usuario:
            posts.pop(i)
            return {"message": "la publicacion fue borrada"}
    return "received"


@app.put("/posts/{post_id_usuario}")
def actualizar_post(post_id_usuario: str, actualizacion_post: User):
    for i, post in enumerate(posts):
        if post["id_usuario"] == post_id_usuario:
            posts[i]["nombre_usuario"] = actualizacion_post.nombre_usuario
            posts[i]["apellido_usuario"] = actualizacion_post.apellido_usuario
            posts[i]["edad"] = actualizacion_post.edad
            return {"message": "la publicacion fue actualizada"}
    raise HTTPException(status_code=404,
                        detail="post not found")
















