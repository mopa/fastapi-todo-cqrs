from sqlalchemy.orm import Session
from src.models.todo import Todo
from src.queries.types.list_todos import ListTodosQuery
from src.buses import get_query_bus

query_bus = get_query_bus()


@query_bus.register_handler(ListTodosQuery)
def list_todos_handler(query: ListTodosQuery, db: Session):
    return db.query(Todo).all()
