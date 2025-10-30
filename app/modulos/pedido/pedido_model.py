from sqlalchemy import Column, String, Integer, Float, ForeignKey
from repositorio.banco_dados import Base

class Pedido(Base):
    __tablename__: str = "pedido"

    id_pedido: int = Column("id_pedido", Integer, primary_key=True, autoincrement=True)
    status: str = Column("status", String)
    id_usuario: int = Column("id_usuario", ForeignKey("usuario.id_usuario"))
    preco: float = Column("preco", Float)

    def __init__(self, usuario: int):
        self.id_usuario = usuario
        self.preco: float = 0
        self.status: str = "PENDENTE"