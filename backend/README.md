# Backend - Internship Assignment API

## 📌 Overview
This is the **FastAPI backend** for the internship assignment.  
It provides user authentication, role-based access, and CRUD APIs for managing tasks.  
The backend connects to a **PostgreSQL database** using SQLAlchemy ORM.

---

## ⚙️ Tech Stack
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **Auth**: JWT (JSON Web Tokens) with `python-jose`
- **Validation**: Pydantic v2
- **Password Hashing**: Passlib (bcrypt)

---

## 📂 Project Structure

backend/ │ ├── app/ │   ├── main.py           # Entry point for FastAPI │   ├── models.py         # Database tables (User, Task) │   ├── schemas.py        # Data validation (Pydantic models) │   ├── auth.py           # Authentication (register, login, JWT) │   ├── crud.py           # Database operations (CRUD functions) │   ├── routes.py         # API endpoints (URLs) │   └── database.py       # Database connection + session │ ├── requirements.txt      # Python dependencies ├── .env.example          # Environment variables template └── README.md             # Backend setup instructions


---

## 🔑 Environment Variables
Create a `.env` file in the `backend/` directory based on `.env.example`:

SECRET_KEY=your_secret_key_here DATABASE_URL=postgresql://username:password@localhost:5432/intern_db

- `SECRET_KEY` → any long random string (used for JWT signing).  
- `DATABASE_URL` → PostgreSQL connection string.

---

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/intern-assignment.git
cd intern-assignment/backend



- `SECRET_KEY` → any long random string (used for JWT signing).  
- `DATABASE_URL` → PostgreSQL connection string.

---

## 🛠️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/intern-assignment.git
cd intern-assignment/backend

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Copy .env.example → .env and update values.

5. Run the server
uvicorn app.main:app --reload

📖 API Endpoints
Health
- GET / → Backend running check
- GET /test-env → Verify environment variables
Auth
- POST /api/v1/register → Register new user
- POST /api/v1/login → Login and get JWT
Tasks
- GET /api/v1/tasks → List tasks (user only)
- POST /api/v1/tasks → Create task
- PUT /api/v1/tasks/{task_id} → Update task (owner only)
- DELETE /api/v1/tasks/{task_id} → Delete task (admin only)

📸 Testing
- Open Swagger UI at:
http://127.0.0.1:8000/docs
- Register a user → Login → Authorize with JWT → Create/List/Update/Delete tasks.

