from app.internal.database import Connection

def get_db():
    db = Connection.get()
    try:
        yield db
    finally:
        Connection.close()