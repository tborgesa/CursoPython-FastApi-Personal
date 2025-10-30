from modulos.pedido.pedido_repo import PedidoRepo
from modulos.pedido.pedido_model import Pedido


class PedidoService:
    async def criar_pedido(id_usuario: int) -> int:
       pedido: Pedido = Pedido(id_usuario)
       await PedidoRepo.insert(pedido)
       return pedido.id