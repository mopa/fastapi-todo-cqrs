from .command_bus import CommandBus
from .query_bus import QueryBus

command_bus_instance = CommandBus()
query_bus_instance = QueryBus()

def get_command_bus() -> CommandBus:
    return command_bus_instance

def get_query_bus() -> QueryBus:
    return query_bus_instance
