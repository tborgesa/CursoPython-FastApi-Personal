from modulos.pedido.pedido_schemas import CriarPedidoBody, CriarPedidoResponse
from modulos.pedido.pedido_repo import PedidoRepo
from modulos.pedido.pedido_model import Pedido


class PedidoService:
    async def criar_pedido(body: CriarPedidoBody) -> int:
       pedido: Pedido = Pedido(body.id_usuario)
       await PedidoRepo.insert(pedido)
       return CriarPedidoResponse.model_validate(pedido)