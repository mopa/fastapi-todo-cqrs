from sqlalchemy.orm import Session
from src.models.todo import Todo
from src.commands.types.create_todo import CreateTodoCommand
from src.buses import get_command_bus

command_bus = get_command_bus()

@command_bus.register_handler(CreateTodoCommand)
def create_todo_handler(command: CreateTodoCommand, db: Session):
    todo = Todo(title=command.title, description=command.description, completed=command.completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
