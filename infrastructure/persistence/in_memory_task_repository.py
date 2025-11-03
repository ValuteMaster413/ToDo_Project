from __future__ import annotations
from typing import Dict, Iterable, Optional

from application.common.abstractions.repositories.task_repository import TaskRepositoryInterface
from domain.entities.task import Task
from domain.value_objects.task_id import TaskId

class InMemoryTodoRepository(TaskRepositoryInterface):
    def __init__(self) -> None:
        self._storage: Dict[str, Task] = {}

    def next_id(self) -> TaskId:
        return TaskId.new()

    def add(self, todo: Task) -> None:
        self._storage[str(todo.id)] = todo

    def get_by_id(self, todo_id: TaskId) -> Optional[Task]:
        return self._storage.get(str(todo_id))

    def list_all(self) -> Iterable[Task]:
        return list(self._storage.values())
    
    def update(self, todo: Task) -> None:
        key = str(todo.id)
        if key not in self._storage:
            raise KeyError(f"Todo {key} not found.")
        self._storage[key] = todo

    def delete(self, todo_id: TaskId) -> None:
        self._storage.pop(str(todo_id), None)
