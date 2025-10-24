import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod

class CreateTaskUseCaseInterface(ABC):
    @abstractmethod
    def execute(self, request_model: "CreateTaskRequestModel") -> "CreateTaskResponseModel":
        pass

@dataclass
class CreateTaskRequestModel(): 
    title: str

@dataclass
class CreateTaskResponseModel():
    id: int = None
    title: str =  None
    done: bool = False
    created_at: datetime.datetime = None
