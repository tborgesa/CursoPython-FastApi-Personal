from fastapi import APIRouter

pedido_router: APIRouter = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedido_router.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}