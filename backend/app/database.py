from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Load from environment or fallback
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:FARHAN@localhost:5432/intern_db")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for getting DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()