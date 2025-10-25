from modulos.usuario.usuario_model import Usuario

async def insert(usuario, session):
    session.add(usuario)
    session.commit()

async def select_email(email,session):
    return session.query(Usuario).filter(Usuario.email==email).first()
