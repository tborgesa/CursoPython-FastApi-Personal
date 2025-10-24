from sqlalchemy import Column, String, Integer, Float, ForeignKey
from repositorio.banco_dados import Base

class Pedido(Base):
    __tablename__ = "pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuario.id"))
    preco = Column("preco", Float)

    def __init__(self, usuario):
        self.usuario = usuario
        self.preco = 0
        self.status = "PENDENTE"