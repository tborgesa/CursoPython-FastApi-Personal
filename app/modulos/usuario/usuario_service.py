from modulos.usuario.usuario_model import Usuario
import modulos.usuario.usuario_repo as repo

async def criar_usuario(email, senha, nome):
    usuario = await repo.select_email(email)
    if usuario:
        return {"mensagem": "já existe um usuário com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        await repo.insert(novo_usuario)
        return {"mensagem": "usuário cadastrado com sucesso"}