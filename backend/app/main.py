import os
from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import router

app = FastAPI(title="Intern Assignment API", version="1.0.0")

models.Base.metadata.create_all(bind=engine)
app.include_router(router)

@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Backend is running successfully!"}

# Test .env
@app.get("/test-env", tags=["Health"])
def test_env():
    return {"SECRET_KEY": os.getenv("SECRET_KEY")}