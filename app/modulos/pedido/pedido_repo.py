from repositorio.banco_dados import get_session
from modulos.pedido.pedido_model import Pedido
from sqlalchemy.orm import sessionmaker

class PedidoRepo:
    async def insert(pedido: Pedido) -> None:
        session: sessionmaker = next(get_session())
        session.add(pedido)
        session.commit()