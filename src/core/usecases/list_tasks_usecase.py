import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod

class ListTasksUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, request_model: "ListTasksRequestModel") -> "ListTasksResponseModel":
        pass

@dataclass
class ListTasksRequestModel(): 
    pass

@dataclass
class ListedTaskModel():
    id: int = None
    title: str =  None
    done: bool = False
    created_at: datetime.datetime = None

@dataclass
class ListTasksResponseModel():
    tasks: list[ListedTaskModel]
