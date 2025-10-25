from fastapi import APIRouter, Depends
from dependencias import database_dependencie as dep
from modulos.usuario import usuario_service

usuario_router = APIRouter(prefix="/usuario", tags=["usuario"])

@usuario_router.get("/autenticar")
async def autenticar():
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@usuario_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(dep.pegar_sessao)):
    return await usuario_service.criar_usuario(email,senha,nome,session)