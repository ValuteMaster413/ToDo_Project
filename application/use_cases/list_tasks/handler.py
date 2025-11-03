from __future__ import annotations
from typing import Final

from application.common.abstractions.repositories.task_repository import TaskRepositoryInterface
from application.use_cases.list_tasks.dto import ListTasksQuery, ListTasksResult, TaskItem

class ListTasksHandler:
    def __init__(self, repo: TaskRepositoryInterface) -> None:
        self._repo: Final[TaskRepositoryInterface] = repo

    def execute(self, q: ListTasksQuery) -> ListTasksResult:
        todos = self._repo.list_all()
        items = [TaskItem(id=str(t.id), title=t.title, completed=t.done) for t in todos]
        return ListTasksResult(items=items)
