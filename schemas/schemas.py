from pydantic import BaseModel
from typing import Optional


class Usuario_BM(BaseModel):
    id: Optional[int] 
    name: str
    login: str
    password: str
    perfil: str