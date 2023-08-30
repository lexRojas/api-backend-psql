from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware



# from routes.notario.actos import actos
# from routes.notario.registros import registros
# from routes.notas_app.estudiante import estudiante
# from routes.notas_app.notas import notas
# from routes.notas_app.calendario import calendario
from routes.route_user import route_user
from routes.route_presupuesto import route_presupuesto



app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def read_root():
    return 'hola a todos '
    

app.include_router(route_user)
app.include_router(route_presupuesto)
# app.include_router(registros)
# app.include_router(actos)
# app.include_router(estudiante)
# app.include_router(notas)
# app.include_router(calendario)

