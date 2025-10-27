from modulos.usuario.usuario_model import Usuario
from repositorio.banco_dados import get_session
from sqlalchemy.orm import sessionmaker

class UsuarioRepo:
    async def insert(usuario: Usuario) -> None:
        session: sessionmaker = next(get_session())
        session.add(usuario)
        session.commit()

    async def select_email(email: str) -> Usuario:
        session: sessionmaker = next(get_session())
        return session.query(Usuario).filter(Usuario.email==email).first()