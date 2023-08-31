
from fastapi import APIRouter
from fastapi import Depends,HTTPException
from sqlalchemy import select,exc

from config.db import AsyncSession, get_db
from models.modelos import tb_usuario
from schemas.schemas import Tb_Usuario_BM

route_usuarios = APIRouter()


@route_usuarios.post("/tb_usuario")
async def set_usuarios(user: Tb_Usuario_BM, db: AsyncSession = Depends(get_db)) :
    try:
        db_table = tb_usuario( 
                                nombre= user.nombre,
                                password=user.password,
                                fecha_vencimiento=user.fecha_vencimiento,
                                fecha_cambio =user.fecha_cambio,
                                login =user.login,
                                activo =user.activo
                            )
        db.add(db_table)
        await db.commit()
        await db.refresh(db_table)
        return db_table.login
    except exc.IntegrityError:
        raise HTTPException(status_code=422, detail="Key Duplicate!!!")
        

@route_usuarios.get("/tb_usuario")
async def get_usuarios(db: AsyncSession = Depends(get_db)) :
    results = await db.execute(select(tb_usuario))
    records = results.scalars().all()
    return records
    