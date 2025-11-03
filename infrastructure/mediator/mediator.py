from __future__ import annotations
from typing import Any, Callable, Dict, Type

from .exceptions import HandlerNotFound

class Mediator:
    def __init__(self) -> None:
        self._handlers: Dict[Type[Any], Callable[[Any], Any]] = {}

    def register(self, message_type: Type[Any], handler: Callable[[Any], Any]) -> None:
        self._handlers[message_type] = handler

    def send(self, message: Any) -> Any:
        msg_type = type(message)
        if msg_type not in self._handlers:
            raise HandlerNotFound(f"No handler registered for {msg_type.__name__}")
        return self._handlers[msg_type](message)
