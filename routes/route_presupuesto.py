
from fastapi import APIRouter
from fastapi import Depends,HTTPException
from sqlalchemy import select,exc

from config.db import AsyncSession, get_db
from models.modelos import tb_presupuesto
from schemas.schemas import tb_presupuesto_BM

route_presupuesto = APIRouter()

@route_presupuesto.get("/tb_presupuesto")
async def get_presupuesto(db: AsyncSession = Depends(get_db)) :
    results = await db.execute(select(tb_presupuesto).order_by(tb_presupuesto.fecha_cambio.desc()).limit(10))
    records = results.scalars().all()
    return records
    