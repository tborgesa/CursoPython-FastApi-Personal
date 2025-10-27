from modulos.usuario.usuario_model import Usuario
from modulos.usuario.usuario_repo import UsuarioRepo
from utilitarios.crypt import get_hash
from utilitarios.notification import Notification

class UsuarioService:
    async def criar_usuario(email: str, senha: str, nome: str) -> Notification:
        notification: Notification = Notification()
        usuario: Usuario = await UsuarioRepo.select_email(email)
        if usuario:
            notification.add_notification("Já existe um usuário com esse email")
        else:
            senha_hash: str = get_hash(senha)
            novo_usuario: Usuario = Usuario(nome, email, senha_hash)
            await UsuarioRepo.insert(novo_usuario)

        return notification