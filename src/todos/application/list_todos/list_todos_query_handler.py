from sqlalchemy.orm import Session
from src.todos.domain.entity import Todo
from src.todos.application.list_todos.list_todos_query import ListTodosQuery
from src.shared.domain.buses import get_query_bus

query_bus = get_query_bus()


@query_bus.register_handler(ListTodosQuery)
def list_todos_handler(query: ListTodosQuery, db: Session):
    return db.query(Todo).all()
