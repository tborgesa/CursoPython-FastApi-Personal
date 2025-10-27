from modulos.usuario.usuario_model import Usuario
from modulos.usuario.usuario_repo import UsuarioRepo
from utilitarios.Crypt import get_hash

class UsuarioService:
    async def criar_usuario(email: str, senha: str, nome: str) -> dict[str,str]:
        usuario: Usuario = await UsuarioRepo.select_email(email)
        if usuario:
            return {"mensagem": "já existe um usuário com esse email"}
        else:
            senha_hash: str = get_hash(senha)
            novo_usuario: Usuario = Usuario(nome, email, senha_hash)
            await UsuarioRepo.insert(novo_usuario)
            return {"mensagem": "usuário cadastrado com sucesso"}