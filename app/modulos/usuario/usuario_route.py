from fastapi import APIRouter, Depends

usuario_router = APIRouter(prefix="/usuario", tags=["usuario"])

@usuario_router.get("/autenticar")
async def home():
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}
