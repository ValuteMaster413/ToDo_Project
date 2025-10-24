from core.usecases.list_tasks_usecase import ListTasksUseCaseInterface, ListTasksResponseModel, ListedTaskModel
from core.entities.task import Task

class ListTasksInteractor(ListTasksUseCaseInterface):
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, request_model):
        tasks = self.task_repository.list_all()
        mapped_tasks = [ListedTaskModel(id=t.id, title=t.title, done=t.done, created_at=t.created_at) for t in tasks]
    
        return ListTasksResponseModel(tasks=mapped_tasks)
