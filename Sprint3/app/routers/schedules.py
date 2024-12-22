from fastapi import APIRouter, Depends
from app.dependencies import get_db

router = APIRouter()

@router.get(
    "/",
    summary="Listar horarios",
    description="Devuelve una lista con todos los horarios registrados en el sistema."
)
def get_schedules(db = Depends(get_db)):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Horari")
        schedules = cursor.fetchall()
        return {"ok": True, "schedules": schedules}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@router.post(
    "/",
    summary="Añadir horario",
    description="Permite registrar un nuevo horario en el sistema."
)
def add_schedule(id_assignatura: int, id_usuari: int, id_aula: int, hora_inici: str, hora_fi: str, dia_setmana: str, db = Depends(get_db)):
    try:
        cursor = db.cursor()
        query = """
            INSERT INTO Horari (id_assignatura, id_usuari, id_aula, hora_inici, hora_fi, dia_setmana)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (id_assignatura, id_usuari, id_aula, hora_inici, hora_fi, dia_setmana))
        db.commit()
        return {"ok": True, "msg": "Schedule added successfully"}
    except Exception as e:
        return {"ok": False, "error": str(e)}