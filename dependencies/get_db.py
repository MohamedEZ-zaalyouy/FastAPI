from database.db import connect, sponsored

def get_db():
    db = sponsored
    try:
        yield db
    finally:
        db.close()