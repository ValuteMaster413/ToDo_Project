from __future__ import annotations
from typing import Final

from application.common.abstractions.repositories.task_repository import TaskRepositoryInterface
from application.use_cases.get_task_by_id.dto import GetTaskByIdQuery, GetTaskByIdResult
from domain.value_objects.task_id import TaskId

class GetTaskByIdHandler:
    def __init__(self, repo: TaskRepositoryInterface) -> None:
        self._repo: Final[TaskRepositoryInterface] = repo

    def execute(self, q: GetTaskByIdQuery) -> GetTaskByIdResult:
        todo_id = TaskId.from_str(q.id)

        todo = self._repo.get_by_id(todo_id)
        if todo is None:
            raise ValueError("Todo not found.")

        return GetTaskByIdResult(
            id=str(todo.id),
            title=todo.title,
            completed=todo.done
        )
