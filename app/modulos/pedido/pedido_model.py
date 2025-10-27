from sqlalchemy import Column, String, Integer, Float, ForeignKey
from repositorio.banco_dados import Base

class Pedido(Base):
    __tablename__: str = "pedido"

    id: int = Column("id", Integer, primary_key=True, autoincrement=True)
    status: str = Column("status", String)
    usuario: int = Column("usuario", ForeignKey("usuario.id"))
    preco: float = Column("preco", Float)

    def __init__(self, usuario: str):
        self.usuario = usuario
        self.preco: float = 0
        self.status: str = "PENDENTE"