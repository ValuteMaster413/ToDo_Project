import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod

class CompleteTaskUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, request_model: "CompleteTaskRequestModel") -> "CompleteTaskResponseModel":
        pass

@dataclass
class CompleteTaskRequestModel(): 
    task_id: int

@dataclass
class CompleteTaskResponseModel():
    id: int = None
    title: str =  None
    done: bool = False
    created_at: datetime.datetime = None
