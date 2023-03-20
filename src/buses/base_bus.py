from abc import ABC
from typing import Type, Callable, Dict, TypeVar

T = TypeVar("T")


class BaseBus(ABC):
    def __init__(self):
        self.handlers: Dict[Type[T], Callable] = {}

    def execute(self, message_type: Type[T], message: T, *args, **kwargs):
        handler = self.handlers.get(message_type)
        if handler is None:
            raise ValueError(f"No handler registered for message type '{message_type.__name__}'")
        return handler(message, *args, **kwargs)

    def register(self, message_type: Type[T], handler: Callable):
        self.handlers[message_type] = handler

    def register_handler(self, message_type: Type[T]):
        def decorator(handler: Callable):
            self.register(message_type, handler)
            return handler

        return decorator