from sqlalchemy.orm import Session
from src.todos.domain.entity import Todo
from src.todos.application.create.create_todo_command import CreateTodoCommand
from src.shared.domain.buses import get_command_bus

command_bus = get_command_bus()

@command_bus.register_handler(CreateTodoCommand)
def create_todo_handler(command: CreateTodoCommand, db: Session):
    todo = Todo(title=command.title, description=command.description, completed=command.completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
