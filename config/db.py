from sqlalchemy import create_engine, MetaData
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from models.modelos import DataBaseModel 






#---LOCAL DATABASE ----

# _hostname ='localhost'
# _username ='basedatos'
# _password ='basedatos'
# _database ='notario'

    #---HEROKU DATABASE ----

_hostname = 'sour-hawthorn.db.elephantsql.com'
_username = 'wficixke'
_password = 'pdeYA4t0t2psZcZL87t6zPjNpNQ5e0Jt'
_database = 'millerdb' 


# SQLALCHEMY 
#engine = create_async_engine("mysql+asyncmy://"+_username + ":"+ _password +"@"+ _hostname +":3306/" + _database)
engine = create_async_engine("postgresql+asyncpg://"+_username + ":"+ _password +"@"+ _hostname +":5432/" + _database)
SessionLocal = async_sessionmaker(engine)



async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(DataBaseModel.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()







# Connect to the database MODO ANTIGUO 
# conn = pymysql.connect(host=_hostname ,
#                              user=_username,
#                              password=_password,
#                              database=_database,
#                              cursorclass=pymysql.cursors.DictCursor)

