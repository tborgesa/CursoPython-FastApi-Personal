from sqlalchemy import Column, String, Integer, Boolean
from repositorio.banco_dados import Base

class Usuario(Base):
    __tablename__: str = "usuario"

    id_usuario: int = Column("id_usuario", Integer, primary_key=True, autoincrement=True)
    nome: str = Column("nome", String, nullable=False)
    email: str = Column("email", String, nullable=False)
    senha: str = Column("senha", String)
    ativo: bool = Column("ativo", Boolean, default=True)
    admin: bool = Column("admin", Boolean, default=False)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo: bool = True
        self.admin: bool = False