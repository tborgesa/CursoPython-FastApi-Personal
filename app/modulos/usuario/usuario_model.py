from sqlalchemy import Column, String, Integer, Boolean
from repositorio.banco_dados import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = True
        self.admin = False