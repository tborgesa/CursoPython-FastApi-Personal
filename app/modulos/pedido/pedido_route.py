from fastapi import APIRouter
from modulos.pedido.pedido_schemas import CriarPedidoBody, CriarPedidoResponse
from modulos.pedido.pedido_service import PedidoService

pedido_router: APIRouter = APIRouter(prefix="/pedidos", tags=["pedidos"])

@pedido_router.post("/criar-pedido", response_model=CriarPedidoResponse)
async def pedidos(body: CriarPedidoBody):
    return await PedidoService.criar_pedido(body)