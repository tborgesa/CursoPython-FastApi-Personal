from modulos.usuario.usuario_model import Usuario
from modulos.usuario.usuario_repo import UsuarioRepo
from utilitarios.crypt import get_hash
from utilitarios.notification import Notification
from modulos.usuario.usuario_schema import CriarContaBody,CriarContaResponse, CriarContaResponseWN

class UsuarioService:
    async def criar_conta(body: CriarContaBody) -> CriarContaResponseWN:
        notification: Notification = Notification()
        usuario: Usuario = await UsuarioRepo.select_email(body.email)
        response: CriarContaResponse = None
        if usuario:
            notification.add_notification("Já existe um usuário com esse email")
        else:
            senha_hash: str = get_hash(body.senha)
            novo_usuario: Usuario = Usuario(body.nome, body.email, senha_hash)
            await UsuarioRepo.insert(novo_usuario)
            response = CriarContaResponse.model_validate(novo_usuario)

        return CriarContaResponseWN(notification,response)