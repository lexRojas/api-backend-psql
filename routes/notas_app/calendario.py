from fastapi import APIRouter
from config.db  import conn

calendario = APIRouter();

@calendario.get("/calendario")
async def getCalendario():
      with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM calendario;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return(result)