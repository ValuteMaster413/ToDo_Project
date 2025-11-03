from abc import ABC, abstractmethod
from domain.entities.task import Task
from typing import Iterable, Optional
from domain.entities.task import Task
from domain.value_objects.task_id import TaskId

class TaskRepositoryInterface(ABC):
    @abstractmethod
    def add (self, task: Task) -> Task:
        pass

    @abstractmethod
    def update(self, task:Task) -> Task:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> None:
        pass

    @abstractmethod
    def list_all(self) -> Iterable[Task]: 
        pass

    @abstractmethod
    def get_by_id(self, task_id: TaskId) -> Optional[Task]:
        pass

    @abstractmethod
    def next_id(self) -> TaskId:
        pass
