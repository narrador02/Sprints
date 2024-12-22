from fastapi import FastAPI
from app.routers import teacher, admin, subjects, schedules, students

app = FastAPI(
    title="API JUM",
    description="API REST para gestionar asignaturas, horarios y asistencia.",
)


app.include_router(teacher.router, prefix="/teacher", tags=["Profesores"])
app.include_router(admin.router, prefix="/admin", tags=["Administradores"])
app.include_router(subjects.router, prefix="/subjects", tags=["Asignaturas"])
app.include_router(schedules.router, prefix="/schedules", tags=["Horarios"])
app.include_router(students.router, prefix="/students", tags=["Alumnos"])