from typing import Generator 

from app.db.session import SessionLoacal

def get_db() -> Generator:
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()