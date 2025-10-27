from modulos.usuario.usuario_model import Usuario
from modulos.usuario.usuario_repo import UsuarioRepo
from utilitarios.crypt import get_hash
from utilitarios.notification import Notification
from modulos.usuario.usuario_schema import UsuarioSchema

class UsuarioService:
    async def criar_usuario(usuario_schema: UsuarioSchema) -> Notification:
        notification: Notification = Notification()
        usuario: Usuario = await UsuarioRepo.select_email(usuario_schema.email)
        if usuario:
            notification.add_notification("Já existe um usuário com esse email")
        else:
            senha_hash: str = get_hash(usuario_schema.senha)
            novo_usuario: Usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_hash)
            await UsuarioRepo.insert(novo_usuario)

        return notification