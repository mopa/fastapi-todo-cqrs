from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.models.schemas import TodoCreate
from src.models.schemas import TodoUpdate

from src.dependencies import get_db_session

from src.buses import CommandBus, QueryBus, get_command_bus, get_query_bus

from src.commands.types.create_todo import CreateTodoCommand
from src.commands.types.update_todo import UpdateTodoCommand
from src.commands.types.delete_todo import DeleteTodoCommand

# Import the command and query handlers to execute decorators (noqa)
import src.commands.handlers  # noqa
import src.queries.handlers  # noqa

from src.queries.types.get_todo import GetTodoQuery
from src.queries.types.list_todos import ListTodosQuery

app = FastAPI()


@app.post("/todos/")
async def create_todo_endpoint(
        todo_create: TodoCreate,
        command_bus: CommandBus = Depends(get_command_bus),
        db: Session = Depends(get_db_session)
) -> None:
    command = CreateTodoCommand(**todo_create.dict())
    return command_bus.execute(CreateTodoCommand, command, db)


@app.get("/todos/{todo_id}")
async def get_todo_endpoint(
        todo_id: int,
        query_bus: QueryBus = Depends(get_query_bus),
        db: Session = Depends(get_db_session)
) -> None:
    query = GetTodoQuery(id=todo_id)
    return query_bus.execute(GetTodoQuery, query, db)


@app.get("/todos/")
async def list_todos_endpoint(
        query_bus: QueryBus = Depends(get_query_bus),
        db: Session = Depends(get_db_session)
) -> None:
    query = ListTodosQuery()
    return query_bus.execute(ListTodosQuery, query, db)


@app.put("/todos/{todo_id}")
async def update_todo_endpoint(
        todo_id: int,
        todo_update: TodoUpdate,
        command_bus: CommandBus = Depends(get_command_bus),
        db: Session = Depends(get_db_session)
) -> None:
    command = UpdateTodoCommand(id=todo_id, **todo_update.dict())
    return command_bus.execute(UpdateTodoCommand, command, db)


@app.delete("/todos/{todo_id}")
async def delete_todo_endpoint(
        todo_id: int,
        command_bus: CommandBus = Depends(get_command_bus),
        db: Session = Depends(get_db_session)
) -> None:
    command = DeleteTodoCommand(id=todo_id)
    return command_bus.execute(DeleteTodoCommand, command, db)
