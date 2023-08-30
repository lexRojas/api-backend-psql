from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select

from config.db import AsyncSession, get_db
from models.modelos import tb_usuario

route_presupuesto = APIRouter()


# @route_user.post("/user")
# async def index(user: Usuario_BM, db: AsyncSession = Depends(get_db)) :
#     db_table_user = TableUser( name=user.name,
#                                login= user.login,
#                                password = user.password,
#                                perfil = user.perfil
#                              )
#     db.add(db_table_user)
#     await db.commit()
#     await db.refresh(db_table_user)
#     return db_table_user.id

@route_presupuesto.get("/tb_usuario")
async def get_presupuesto(db: AsyncSession = Depends(get_db)) :
    results = await db.execute(select(tb_usuario))
    records = results.scalars().all()
    return records
