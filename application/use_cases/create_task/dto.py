from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class CreateTaskCommand:
    title: str

@dataclass(frozen=True)
class CreateTaskResult:
    id: str
    title: str
    completed: bool
