from __future__ import annotations
from typing import Final

from application.common.abstractions.repositories.task_repository import TaskRepositoryInterface
from application.use_cases.toggle_done.dto import ToggleDoneCommand, ToggleDoneResult
from domain.value_objects.task_id import TaskId

class ToggleDoneHandler:
    def __init__(self, repo: TaskRepositoryInterface) -> None:
        self._repo: Final[TaskRepositoryInterface] = repo

    def execute(self, cmd: ToggleDoneCommand) -> ToggleDoneResult:
        todo_id = TaskId.from_str(cmd.id)

        todo = self._repo.get_by_id(todo_id)
        if todo is None:
            raise ValueError("Todo not found.")

        if todo.done:
            todo.mark_undone()
        else:
            todo.mark_done()

        return ToggleDoneResult(id=str(todo.id), completed=todo.done)
