from sqlalchemy.orm import Session
from src.models.todo import Todo
from src.commands.types.update_todo import UpdateTodoCommand
from src.buses import get_command_bus

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
