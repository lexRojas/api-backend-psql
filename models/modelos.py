from sqlalchemy import  String, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional


# declarative base class
class DataBaseModel(DeclarativeBase):
    pass


DataBaseModel.metadata.schema="horas"


# an example mapping using the base
class TableUser(DataBaseModel):
    __tablename__ = "usuario"
    
    id: Mapped[int] = mapped_column(  primary_key=True)
    name: Mapped[str]= mapped_column(String(30))
    login: Mapped[str]= mapped_column(String(30))
    password: Mapped[str]= mapped_column(String(30))
    perfil: Mapped[str]= mapped_column(String(30))
    


    