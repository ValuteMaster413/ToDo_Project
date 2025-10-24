from core.usecases.create_task_usecase import CreateTaskUseCaseInterface, CreateTaskResponseModel
from core.entities.task import Task

class CreateTaskInteractor(CreateTaskUseCaseInterface):
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, request_model):
        task = Task(title=request_model.title)

        saved_task = self.task_repository.add(task)

        response = CreateTaskResponseModel(
            id=saved_task.id,
            title=saved_task.title,
            done=saved_task.done,
            created_at=saved_task.created_at,
        )
    
        return response
