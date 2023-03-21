from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.todos.domain.schemas import TodoCreate
from src.todos.domain.schemas import TodoUpdate

from core.dependencies import get_db_session

from src.shared.domain.buses import CommandBus, QueryBus, get_command_bus, get_query_bus

from src.todos.application.create.create_todo_command import CreateTodoCommand
from src.todos.application.update.update_todo_command import UpdateTodoCommand
from src.todos.application.delete.delete_todo_command import DeleteTodoCommand

# Import the command and query handlers to execute decorators (noqa)
import src.todos.application.create.create_todo_command_handler # noqa
import src.todos.application.update.update_todo_command_handler # noqa
import src.todos.application.delete.delete_todo_command_handler # noqa
import src.todos.application.get_todo.get_todo_query_handler # noqa
import src.todos.application.list_todos.list_todos_query_handler # noqa

from src.todos.application.get_todo.get_todo_query import GetTodoQuery
from src.todos.application.list_todos.list_todos_query import ListTodosQuery

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")
logger.info("**Starting FastAPI Todo CQRS application**")

app = FastAPI()
logger.info("*Application startup*")


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
