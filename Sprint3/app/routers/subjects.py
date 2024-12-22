from fastapi import APIRouter, Depends
from app.dependencies import get_db

router = APIRouter()

@router.get(
    "/teacher/{teacher_id}",
    summary="Obtener asignaturas del profesor",
    description="Devuelve todas las asignaturas asignadas a un profesor específico."
)
def get_teacher_subjects(teacher_id: int, db = Depends(get_db)):
    try:
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM Assignatura WHERE id_usuari = %s"
        cursor.execute(query, (teacher_id,))
        subjects = cursor.fetchall()
        return {"ok": True, "subjects": subjects}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@router.post(
    "/",
    summary="Añadir asignatura",
    description="Permite añadir una nueva asignatura al sistema."
)
def add_subject(nom_assignatura: str, id_usuari: int, db = Depends(get_db)):
    try:
        cursor = db.cursor()
        query = "INSERT INTO Assignatura (nom_assignatura, id_usuari) VALUES (%s, %s)"
        cursor.execute(query, (nom_assignatura, id_usuari))
        db.commit()
        return {"ok": True, "msg": "Asignatura añadida satisfactoriamente."}
    except Exception as e:
        return {"ok": False, "error": str(e)}