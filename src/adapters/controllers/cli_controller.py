from core.usecases.create_task_usecase import CreateTaskRequestModel
from core.usecases.complete_task_usecase import CompleteTaskRequestModel
from core.usecases.list_tasks_usecase import ListTasksRequestModel


class CLIController:
    def __init__(self, create_task_uc, complete_task_uc, list_tasks_uc):
        self.create_task_uc = create_task_uc
        self.complete_task_uc = complete_task_uc
        self.list_tasks_uc = list_tasks_uc

    def create_task(self, title: str):
        request = CreateTaskRequestModel(title=title)
        response = self.create_task_uc.execute(request)

        print(f"[CREATED] id={response.id} | title='{response.title}' | done={response.done} | created_at={response.created_at}")
        return response

    def complete_task(self, task_id: int):
        request = CompleteTaskRequestModel(task_id=task_id)
        response = self.complete_task_uc.execute(request)

        print(f"[COMPLETED] id={response.id} | title='{response.title}' | done={response.done}")
        return response

    def list_tasks(self):
        request = ListTasksRequestModel()
        response = self.list_tasks_uc.execute(request)

        print("[TASKS]")
        for task in response.tasks:
            print(f" - id={task.id} | title='{task.title}' | done={task.done} | created_at={task.created_at}")

        return response
