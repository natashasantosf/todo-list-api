from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter()

@router.post("/todos", response_model=schemas.TodoResponse, status_code=201)
def create_todo(
    todo_data: schemas.TodoCreate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    new_todo = models.Todo(title=todo_data.title, description=todo_data.description, owner_id=current_user.id)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.get("/todos", response_model=schemas.TodoListResponse)
def list_todos(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    
    offset = (page - 1) * limit
    query = db.query(models.Todo).filter(models.Todo.owner_id == current_user.id)
    total = query.count()
    todos = query.offset(offset).limit(limit).all()
    
    return {
        "data": todos,
        "page": page, 
        "limit": limit,
        "total": total
    }

@router.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo_data: schemas.TodoUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    
    if todo.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para editar essa tarefa"
        )
    
    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.description is not None:
        todo.description = todo_data.description
    if todo_data.completed is not None:
        todo.completed = todo_data.completed

    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    
    if todo.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para deletar essa tarefa"
        )
    
    db.delete(todo)
    db.commit()
    return None