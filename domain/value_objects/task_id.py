from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass(frozen=True)
class TaskId:
    value: UUID

    @staticmethod
    def new() -> "TaskId":
        return TaskId(uuid4())

    @staticmethod
    def from_str(raw: str) -> "TaskId":
        return TaskId(UUID(raw))

    def __str__(self) -> str:
        return str(self.value)
