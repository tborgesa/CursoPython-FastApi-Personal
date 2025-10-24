#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

from modulos.pedido.pedido_route import pedido_router
from modulos.usuario.usuario_route import usuario_router

app.include_router(pedido_router)
app.include_router(usuario_router)