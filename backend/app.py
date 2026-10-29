from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="ActivityLeo Multi-DB API", version="1.0.0")

# Habilitar CORS para peticiones desde el Frontend Nginx
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS PYDANTIC ---
class Actividad(BaseModel):
    id: Optional[int] = None
    nombre: str
    categoria: str
    cupo: int

class Alumno(BaseModel):
    id: Optional[int] = None
    nombre: str
    email: str
    grado: str

class Profesor(BaseModel):
    id: Optional[int] = None
    nombre: str
    especialidad: str
    departamento: str

# --- ESTRUCTURAS DE DATOS DE PRUEBA ---
db_mariadb: List[dict] = [
    {"id": 1, "nombre": "Taller de Programación Python", "categoria": "Tecnología", "cupo": 25},
    {"id": 2, "nombre": "Torneo de Ajedrez", "categoria": "Deportes", "cupo": 16},
    {"id": 3, "nombre": "Club de Lectura y Debate", "categoria": "Humanidades", "cupo": 12}
]

db_mysql: List[dict] = [
    {"id": 1, "nombre": "María García", "email": "maria.garcia@example.com", "grado": "3º ESO"},
    {"id": 2, "nombre": "Carlos Rodríguez", "email": "carlos.r@example.com", "grado": "1º Bachillerato"},
    {"id": 3, "nombre": "Laura Martínez", "email": "laura.m@example.com", "grado": "2º Bachillerato"}
]

db_postgres: List[dict] = [
    {"id": 1, "nombre": "Dra. Elena Beltrán", "especialidad": "Inteligencia Artificial", "departamento": "Informática"},
    {"id": 2, "nombre": "Prof. Javier Gómez", "especialidad": "Matemáticas Aplicadas", "departamento": "Ciencias Exactas"},
    {"id": 3, "nombre": "Dra. Carmen Ruiz", "especialidad": "Literatura Hispánica", "departamento": "Lengua y Literatura"}
]

@app.get("/")
def read_root():
    return {"status": "online", "system": "webActivityLeo API"}

# ==================== MARIADB CRUD ====================
@app.get("/api/mariadb/actividades", response_model=List[Actividad])
def get_actividades():
    return db_mariadb

@app.post("/api/mariadb/actividades", response_model=Actividad)
def create_actividad(act: Actividad):
    new_id = max([i["id"] for i in db_mariadb], default=0) + 1
    data = act.dict()
    data["id"] = new_id
    db_mariadb.append(data)
    return data

@app.put("/api/mariadb/actividades/{act_id}", response_model=Actividad)
def update_actividad(act_id: int, act: Actividad):
    for idx, item in enumerate(db_mariadb):
        if item["id"] == act_id:
            updated = act.dict()
            updated["id"] = act_id
            db_mariadb[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Actividad no encontrada")

@app.delete("/api/mariadb/actividades/{act_id}")
def delete_actividad(act_id: int):
    global db_mariadb
    db_mariadb = [i for i in db_mariadb if i["id"] != act_id]
    return {"message": "Actividad eliminada de MariaDB"}

# ==================== MYSQL CRUD ====================
@app.get("/api/mysql/alumnos", response_model=List[Alumno])
def get_alumnos():
    return db_mysql

@app.post("/api/mysql/alumnos", response_model=Alumno)
def create_alumno(alum: Alumno):
    new_id = max([i["id"] for i in db_mysql], default=0) + 1
    data = alum.dict()
    data["id"] = new_id
    db_mysql.append(data)
    return data

@app.put("/api/mysql/alumnos/{alum_id}", response_model=Alumno)
def update_alumno(alum_id: int, alum: Alumno):
    for idx, item in enumerate(db_mysql):
        if item["id"] == alum_id:
            updated = alum.dict()
            updated["id"] = alum_id
            db_mysql[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Alumno no encontrado")

@app.delete("/api/mysql/alumnos/{alum_id}")
def delete_alumno(alum_id: int):
    global db_mysql
    db_mysql = [i for i in db_mysql if i["id"] != alum_id]
    return {"message": "Alumno eliminado de MySQL"}

# ==================== POSTGRESQL CRUD ====================
@app.get("/api/postgres/profesores", response_model=List[Profesor])
def get_profesores():
    return db_postgres

@app.post("/api/postgres/profesores", response_model=Profesor)
def create_profesor(prof: Profesor):
    new_id = max([i["id"] for i in db_postgres], default=0) + 1
    data = prof.dict()
    data["id"] = new_id
    db_postgres.append(data)
    return data

@app.put("/api/postgres/profesores/{prof_id}", response_model=Profesor)
def update_profesor(prof_id: int, prof: Profesor):
    for idx, item in enumerate(db_postgres):
        if item["id"] == prof_id:
            updated = prof.dict()
            updated["id"] = prof_id
            db_postgres[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Profesor no encontrado")

@app.delete("/api/postgres/profesores/{prof_id}")
def delete_profesor(prof_id: int):
    global db_postgres
    db_postgres = [i for i in db_postgres if i["id"] != prof_id]
    return {"message": "Profesor eliminado de PostgreSQL"}

# ==================== REDIS ANALYTICS ====================
@app.get("/api/redis/stats")
def get_redis_stats():
    return {
        "actividades_count": len(db_mariadb),
        "alumnos_count": len(db_mysql),
        "profesores_count": len(db_postgres),
        "cache_status": "ACTIVE"
    }