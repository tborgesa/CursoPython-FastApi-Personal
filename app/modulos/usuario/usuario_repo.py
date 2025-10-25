from modulos.usuario.usuario_model import Usuario
from repositorio.banco_dados import get_session

async def insert(usuario):
    session = next(get_session())
    session.add(usuario)
    session.commit()

async def select_email(email):
    session = next(get_session())
    return session.query(Usuario).filter(Usuario.email==email).first()
