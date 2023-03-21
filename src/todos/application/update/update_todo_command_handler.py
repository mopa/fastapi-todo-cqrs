from sqlalchemy.orm import Session
from src.todos.domain.entity import Todo
from src.todos.application.update.update_todo_command import UpdateTodoCommand
from src.shared.domain.buses import get_command_bus

command_bus = get_command_bus()

@command_bus.register_handler(UpdateTodoCommand)
def update_todo_handler(command: UpdateTodoCommand, db: Session):
    todo = db.query(Todo).filter(Todo.id == command.id).first()
    if not todo:
        return None

    todo.title = command.title or todo.title
    todo.description = command.description or todo.description
    todo.completed = command.completed if command.completed is not None else todo.completed

    db.commit()
    db.refresh(todo)

    return todo
