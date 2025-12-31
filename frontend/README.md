
---

## 📖 `frontend/README.md`

```markdown
# Frontend - React UI

## Overview
This is the frontend interface for the internship assignment.  
It allows users to register/login, access a protected dashboard, and perform CRUD operations on tasks.

---

## Features
- Register & login users
- Store JWT securely in localStorage
- Access protected dashboard (JWT required)
- Create, list, update, delete tasks
- Show error/success messages from API responses

---

## Setup Instructions

### 1. Navigate to frontend folder
```bash
cd intern-assignment/frontend

2. INSTALL DEPENDENCIES
npm install

3.RUN THE DEVELOPMENT SERVER 
npm run dev

4. ACCESS THE APP 
http://localhost:5173


File Structure
- src/App.jsx → Main React component with routing
- src/Login.jsx → Register/Login page
- src/Tasks.jsx → Dashboard with CRUD
- src/api.js → Axios setup for API calls

API CONNECTION 
The frontend connects to the backend at:
http://127.0.0.1:8000/api/v1