from typing import NamedTuple
from pydantic import BaseModel, ConfigDict
from utilitarios.notification import Notification

class CriarContaBody(BaseModel):
    nome: str
    email: str
    senha: str
    model_config = ConfigDict(from_attributes=True)

class CriarContaResponse(BaseModel):
    id_usuario: int
    model_config = ConfigDict(from_attributes=True)

class CriarContaResponseWN(NamedTuple):
    notification: Notification
    response: CriarContaResponse  