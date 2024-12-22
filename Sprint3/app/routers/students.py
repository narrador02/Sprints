from fastapi import APIRouter, Depends
from app.dependencies import get_db

router = APIRouter()

@router.get(
    "/{student_id}",
    summary="Obtener información del estudiante",
    description="Devuelve la información personal de un estudiante específico."
)
def get_student_info(student_id: int, db=Depends(get_db)):
    try:
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM Usuari WHERE id = %s"
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        if result:
            return {"ok": True, "student_info": result}
        return {"ok": False, "msg": "Student not found"}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@router.get(
    "/{student_id}/subjects",
    summary="Obtener asignaturas del estudiante",
    description="Devuelve las asignaturas en las que está matriculado un estudiante específico."
)
def get_student_subjects(student_id: int, db=Depends(get_db)):
    try:
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT a.* FROM Assignatura a
            INNER JOIN UserSubject us ON us.subjectID = a.id
            WHERE us.userID = %s
        """
        cursor.execute(query, (student_id,))
        subjects = cursor.fetchall()
        return {"ok": True, "subjects": subjects}
    except Exception as e:
        return {"ok": False, "error": str(e)}