from core.ports.task_repository import TaskRepositoryInterface
from core.entities.task import Task
from typing import List, Optional

class InMemoryTaskRepository(TaskRepositoryInterface):
    def __init__(self):
        self._storage: dict[int, Task] = {}
        self._next_id = 1

    def add(self, task: Task) -> Task:
        if task.id is None:
            task.id = self._next_id
            self._next_id += 1

        self._storage[task.id] = task
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self._storage.get(task_id)

    def list_all(self) -> List[Task]:
        return list(self._storage.values())

    def update(self, task: Task) -> Task:
        if task.id not in self._storage:
            raise ValueError(f"Task with id={task.id} not found")
        self._storage[task.id] = task
        return task

    def delete(self, task_id: int) -> None:
        if task_id in self._storage:
            del self._storage[task_id]
