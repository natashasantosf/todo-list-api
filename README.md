## 🚀 Task Management API

A secure and scalable REST API for managing tasks with user authentication.

Built using FastAPI, SQLAlchemy, and JWT.

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

▶️ How to Run:
pip install -r requirements.txt
uvicorn app.main:app --reload

📚 API Documentation:

Swagger UI available at:
http://127.0.0.1:8000/docs

💡 Project Purpose:

This project was built to demonstrate backend development skills, including authentication, database management, and API design.

📌 Future Improvements:

- Deployment (Render / Railway)
- Unit tests
- Docker support
- Rate limiting