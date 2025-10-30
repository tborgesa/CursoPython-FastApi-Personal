from pydantic import BaseModel, ConfigDict

class CriarPedidoBody(BaseModel):
    id_usuario: int
    model_config = ConfigDict(from_attributes=True)
    
class CriarPedidoResponse(BaseModel):
    id_pedido: int
    model_config = ConfigDict(from_attributes=True)