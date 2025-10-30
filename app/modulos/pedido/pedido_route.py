from fastapi import APIRouter
from modulos.pedido.pedido_service import PedidoService

pedido_router: APIRouter = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedido_router.post("/criar-pedido/{id_usuario}")
async def pedidos(id_usuario: int):
    return await PedidoService.criar_pedido(id_usuario)