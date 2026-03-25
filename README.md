## 🚀 Task Management API

A secure and scalable REST API for managing tasks with user authentication, built with FastAPI and deployed in production.

🌐 **Live API:**  
https://todo-list-api-2-20rt.onrender.com

📚 **Documentation:**  
https://todo-list-api-2-20rt.onrender.com/redoc

---

🔧 Features:

- User registration and authentication (JWT)
- CRUD operations for tasks
- User-specific data isolation
- Pagination support
- Secure password hashing

🛠 Tech Stack:

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (python-jose)

## ▶️ How to Run:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

---

📚 API Documentation:

- Local: http://127.0.0.1:8000/docs  
- Online: https://todo-list-api-2-20rt.onrender.com/redoc

💡 Project Purpose:

This project was built to demonstrate backend development skills, including authentication, database management, and API design.

📌 Future Improvements:

- Unit tests
- Docker support
- Rate limiting