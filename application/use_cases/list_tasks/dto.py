from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class ListTasksQuery:
    pass

@dataclass(frozen=True)
class TaskItem:
    id: str
    title: str
    completed: bool

@dataclass(frozen=True)
class ListTasksResult:
    items: List[TaskItem]
