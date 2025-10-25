from modulos.usuario.usuario_model import Usuario
import modulos.usuario.usuario_repo as repo

async def criar_usuario(email, senha, nome, session):
    usuario = await repo.select_email(email, session)
    if usuario:
        return {"mensagem": "já existe um usuário com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        await repo.insert(novo_usuario, session)
        return {"mensagem": "usuário cadastrado com sucesso"}