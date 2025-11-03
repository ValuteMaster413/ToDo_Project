from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class GetTaskByIdQuery:
    id: str

@dataclass(frozen=True)
class GetTaskByIdResult:
    id: str
    title: str
    completed: bool
