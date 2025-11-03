from __future__ import annotations
from typing import Final

from application.common.abstractions.repositories.task_repository import TaskRepositoryInterface
from application.use_cases.create_task.dto import CreateTaskCommand, CreateTaskResult
from domain.entities.task import Task

from domain.constants import TITLE_MAX_LEN

class CreateTaskHandler:
    def __init__(self, repo: TaskRepositoryInterface) -> None:
        self._repo: Final[TaskRepositoryInterface] = repo

    def execute(self, cmd: CreateTaskCommand) -> CreateTaskResult:
        title = (cmd.title or "").strip()
        if not title:
            raise ValueError("Title is required.")
        if len(title) > TITLE_MAX_LEN:
            raise ValueError(f"Title must be at most {TITLE_MAX_LEN} characters.")

        new_id = self._repo.next_id()
        task = Task(id=new_id, title=title)
        self._repo.add(task)

        return CreateTaskResult(
            id=str(task.id),
            title=task.title,
            completed=task.done,
        )
