from fastapi import APIRouter
from modulos.usuario.usuario_service import UsuarioService

usuario_router: APIRouter = APIRouter(prefix="/usuario", tags=["usuario"])

@usuario_router.get("/autenticar")
async def autenticar():
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@usuario_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str):
    return await UsuarioService.criar_usuario(email,senha,nome)