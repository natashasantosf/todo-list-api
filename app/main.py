from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users, todos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo List API",
    description="API para gerenciamento de tarefas com autenticação",
    version="1.0.0"
)

app.include_router(users.router)

app.include_router(todos.router)