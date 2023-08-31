from sqlalchemy import  String, Integer, Date, Float
from datetime import date
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
    


DataBaseModel.metadata.schema="public"

class tb_usuario(DataBaseModel):
    __tablename__ = "tb_usuario"
    
    login: Mapped[str] = mapped_column(  primary_key=True)
    nombre: Mapped[str]= mapped_column(String(30))
    password: Mapped[str]= mapped_column(String(8))
    fecha_cambio: Mapped[date] = mapped_column(Date, server_default=func.now())
    fecha_vencimiento:  Mapped[date] = mapped_column(Date, server_default=func.now())
    activo : Mapped[bool]


class tb_presupuesto(DataBaseModel):
    __tablename__ = "tb_presupuesto"

    presupuesto: Mapped[str] = mapped_column( String(7), primary_key=True)
    proyecto: Mapped[str]= mapped_column(String(200))
    propietario: Mapped[str]= mapped_column(String(40))
    fecha_apertura: Mapped[date] = mapped_column(Date, server_default=func.now())
    hora_apertura :Mapped[str]= mapped_column(String(5))
    area_construccion: Mapped[float] = mapped_column(Float)
    fecha_cambio: Mapped[date] = mapped_column(Date, server_default=func.now())
    cod_usuario : Mapped[str]= mapped_column(String(15))
    tipo_licitacion : Mapped[int] = mapped_column(Integer)
    responsable : Mapped[int] = mapped_column(Integer)
    num_licitacion : Mapped[str]= mapped_column(String(20))
    activo: Mapped[bool]