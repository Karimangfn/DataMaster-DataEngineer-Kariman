from pydantic import BaseModel
from typing import List

class Cliente(BaseModel):
    id: str
    nome: str
    email: str
    telefone: str
    compras: List[dict]