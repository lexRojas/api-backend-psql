from sqlalchemy import  String, Integer, DateTime
import datetime
from sqlalchemy.sql import func
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
    


class tb_usuario(DataBaseModel):
    __tablename__ = "tb_usuario"
    schema = 'public'

    login: Mapped[str] = mapped_column(  primary_key=True)
    nombre: Mapped[str]= mapped_column(String(30))
    password: Mapped[str]= mapped_column(String(8))
    fecha_cambio: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    fecha_vencimiento:  Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    activo : Mapped[bool]
    
    