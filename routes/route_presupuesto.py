
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select

from config.db import AsyncSession, get_db
from models.modelos import tb_presupuesto
from schemas.schemas import tb_presupuesto_BM

route_presupuesto = APIRouter()

@route_presupuesto.get("/tb_presupuesto")
async def get_presupuesto(filtro='', db: AsyncSession = Depends(get_db)) :
    search = "%{}%".format(filtro)
    print(search)
    results = await db.execute(select(tb_presupuesto).filter(tb_presupuesto.proyecto.like(search.upper())).order_by(tb_presupuesto.fecha_cambio.desc()).limit(10))
    records = results.scalars().all()
    return records
    