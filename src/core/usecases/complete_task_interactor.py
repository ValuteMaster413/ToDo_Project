from core.usecases.complete_task_usecase import CompleteTaskUseCaseInterface, CompleteTaskResponseModel

class CompleteTaskInteractor(CompleteTaskUseCaseInterface):
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, request_model):
        task_id = request_model.task_id

        completed_task = self.task_repository.get_by_id(task_id)

        if completed_task is None:
            raise ValueError(f"Task with id={task_id} not found")

        completed_task.mark_done()
        self.task_repository.update(completed_task)

        response = CompleteTaskResponseModel(
            id=completed_task.id,
            title=completed_task.title,
            done=completed_task.done,
            created_at=completed_task.created_at,
        )
    
        return response
