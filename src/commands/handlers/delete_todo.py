from sqlalchemy.orm import Session
from src.models.todo import Todo
from src.commands.types.delete_todo import DeleteTodoCommand
from src.buses import get_command_bus

command_bus = get_command_bus()

@command_bus.register_handler(DeleteTodoCommand)
def delete_todo_handler(command: DeleteTodoCommand, db: Session):
    todo = db.query(Todo).filter(Todo.id == command.id).first()
    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return {"status": "success", "message": f"Todo with ID {command.id} has been deleted."}
