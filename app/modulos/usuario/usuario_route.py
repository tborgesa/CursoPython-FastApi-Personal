from fastapi import APIRouter, HTTPException
from modulos.usuario.usuario_service import UsuarioService
from utilitarios.notification import Notification
from modulos.usuario.usuario_schema import UsuarioSchema

usuario_router: APIRouter = APIRouter(prefix="/usuario", tags=["usuario"])

@usuario_router.get("/autenticar")
async def autenticar():
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@usuario_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema):
    notification: Notification = await UsuarioService.criar_usuario(usuario_schema)

    if (notification.has_notification()):
        raise HTTPException(status_code=400,detail=notification.get_notification())