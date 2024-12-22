from fastapi import APIRouter, Depends
from app.dependencies import get_db

router = APIRouter()

@router.get(
    "/{teacher_id}/schedules",
    summary="Obtener horarios del profesor",
    description="Devuelve una lista con todos los horarios asignados a un profesor específico."
)
def get_teacher_schedules(teacher_id: int, db = Depends(get_db)):
    try:
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT h.* FROM Horari h
            INNER JOIN Assignatura a ON h.id_assignatura = a.id
            WHERE a.id_usuari = %s
        """
        cursor.execute(query, (teacher_id,))
        schedules = cursor.fetchall()
        return {"ok": True, "schedules": schedules}
    except Exception as e:
        return {"ok": False, "error": str(e)}