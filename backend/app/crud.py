from sqlalchemy.orm import Session
from app import models
from app.schemas import UserCreate, TaskCreate
from app.auth import hash_password

# Create user
def create_user(db: Session, user: UserCreate):
    db_user = models.User(
        email=user.email,
        hashed_password=hash_password(user.password),
        role="user",  # use string role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Create task
def create_task(db: Session, task: TaskCreate, owner_id: int):
    db_task = models.Task(title=task.title, description=task.description, owner_id=owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get tasks (admin sees all, user sees own)
def get_tasks(db: Session, owner_id: int, is_admin: bool):
    query = db.query(models.Task)
    if not is_admin:
        query = query.filter(models.Task.owner_id == owner_id)
    return query.all()