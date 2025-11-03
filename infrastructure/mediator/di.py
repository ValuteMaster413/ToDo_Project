from __future__ import annotations
from typing import Callable

from infrastructure.mediator.mediator import Mediator

from infrastructure.persistence.in_memory_task_repository import InMemoryTodoRepository

from application.use_cases.create_task.handler import CreateTaskHandler
from application.use_cases.create_task.dto import CreateTaskCommand

from application.use_cases.get_task_by_id.handler import GetTaskByIdHandler
from application.use_cases.get_task_by_id.dto import GetTaskByIdQuery

from application.use_cases.list_tasks.handler import ListTasksHandler
from application.use_cases.list_tasks.dto import ListTasksQuery

from application.use_cases.toggle_done.handler import ToggleDoneHandler
from application.use_cases.toggle_done.dto import ToggleDoneCommand


def build_default_mediator() -> Mediator:
    repo = InMemoryTodoRepository()

    create = CreateTaskHandler(repo)
    get_by_id = GetTaskByIdHandler(repo)
    list_all = ListTasksHandler(repo)
    toggle = ToggleDoneHandler(repo)

    m = Mediator()

    m.register(CreateTaskCommand, lambda cmd: create.execute(cmd))
    m.register(GetTaskByIdQuery, lambda q: get_by_id.execute(q))
    m.register(ListTasksQuery,   lambda q: list_all.execute(q))
    m.register(ToggleDoneCommand, lambda cmd: toggle.execute(cmd))

    return m
