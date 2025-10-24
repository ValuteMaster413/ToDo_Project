from abc import ABC, abstractmethod
from core.entities.task import Task
from typing import List

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
    def list_all(self) -> List[Task]: 
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Task:
        pass