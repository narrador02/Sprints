from fastapi import APIRouter, Depends
from app.dependencies import get_db

router = APIRouter()

@router.get(
    "/subjects",
    summary="Listar asignaturas",
    description="Devuelve una lista de todas las asignaturas disponibles en la base de datos."
)
def get_all_subjects(db = Depends(get_db)):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Assignatura")
        subjects = cursor.fetchall()
        return {"ok": True, "subjects": subjects}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@router.post(
    "/subjects",
    summary="Añadir asignatura",
    description="Permite añadir una nueva asignatura a la base de datos."
)
def add_subject(nom_assignatura: str, id_usuari: int, db = Depends(get_db)):
    try:
        cursor = db.cursor()
        query = "INSERT INTO Assignatura (nom_assignatura, id_usuari) VALUES (%s, %s)"
        cursor.execute(query, (nom_assignatura, id_usuari))
        db.commit()
        return {"ok": True, "msg": "Subject added successfully"}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@router.delete(
    "/subjects/{id}",
    summary="Eliminar asignatura",
    description="Elimina una asignatura específica identificada por su ID."
)
def delete_subject(id: int, db = Depends(get_db)):
    try:
        cursor = db.cursor()
        query = "DELETE FROM Assignatura WHERE id = %s"
        cursor.execute(query, (id,))
        db.commit()
        return {"ok": True, "msg": "Subject deleted successfully"}
    except Exception as e:
        return {"ok": False, "error": str(e)}