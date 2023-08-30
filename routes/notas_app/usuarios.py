from fastapi import APIRouter
from config.db  import conn

notas = APIRouter();

@notas.get("/usuario/{login}")
async def getNotas(login = "-1"):
      with conn.cursor() as cursor:
        # Read a single record
        if (id=="-1"):
          sql = "select * from usuarios" 
        else:
          sql = "SELECT * FROM  usuarios n where n.login ="+ str(login) + ";"
        cursor.execute(sql)
        result = cursor.fetchall()
        return(result)