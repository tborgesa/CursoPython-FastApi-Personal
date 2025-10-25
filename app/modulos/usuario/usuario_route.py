from fastapi import APIRouter, Depends
from modulos.usuario.usuario_model import Usuario
from dependencias.database_dependencie import pegar_sessao

usuario_router = APIRouter(prefix="/usuario", tags=["usuario"])

@usuario_router.get("/autenticar")
async def autenticar():
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@usuario_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        return {"mensagem": "já existe um usuário com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuário cadastrado com sucesso"}