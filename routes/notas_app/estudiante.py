from fastapi import APIRouter
from config.db  import conn

estudiante = APIRouter();

@estudiante.get("/estudiante")
async def getEstudiante(id = "-1"):
      with conn.cursor() as cursor:
        # Read a single record
        if (id=="-1"):
          sql = "select * from estudiante" 
        else:
          sql = "select * from estudiante e where e.id ="+ str(id)
        cursor.execute(sql)
        result = cursor.fetchall()
        return(result)