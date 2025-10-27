from sqlalchemy import Column, String, Integer, Float, ForeignKey
from repositorio.banco_dados import Base

class PedidoItem(Base):
    __tablename__: str = "pedido_item"

    id: int = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade: int = Column("quantidade", Integer)
    sabor: str = Column("sabor", String)
    tamanho: str = Column("tamanho", String)
    preco_unitario: float = Column("preco_unitario", Float)
    pedido: int = Column("pedido", ForeignKey("pedido.id"))

    def __init__(self, quantidade: int, sabor: str, tamanho: str, preco_unitario: float, pedido: int):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido