from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.todos.domain.entity import Todo
from src.todos.application.get_todo.get_todo_query import GetTodoQuery
from src.shared.domain.buses import get_query_bus

query_bus = get_query_bus()

@query_bus.register_handler(GetTodoQuery)
def get_todo_handler(query: GetTodoQuery, db: Session):
    todo = db.query(Todo).filter(Todo.id == query.id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
