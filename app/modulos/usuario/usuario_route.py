from fastapi import APIRouter, HTTPException
from modulos.usuario.usuario_service import UsuarioService
from utilitarios.notification import Notification
from modulos.usuario.usuario_schema import CriarContaBody, CriarContaResponse, CriarContaResponseWN

usuario_router: APIRouter = APIRouter(prefix="/usuario", tags=["usuario"])

@usuario_router.get("/autenticar")
async def autenticar():
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@usuario_router.post("/criar_conta", response_model=CriarContaResponse)
async def criar_conta(body: CriarContaBody):
    responseWN: CriarContaResponseWN = await UsuarioService.criar_conta(body)

    if (responseWN.notification.has_notification()):
        raise HTTPException(status_code=400,detail=responseWN.notification.get_notification())
    
    return responseWN.response;