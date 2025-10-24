from adapters.repositories.in_memory_task_repository import InMemoryTaskRepository
from core.usecases.create_task_interactor import CreateTaskInteractor
from core.usecases.complete_task_interactor import CompleteTaskInteractor
from core.usecases.list_tasks_interactor import ListTasksInteractor
from adapters.controllers.cli_controller import CLIController


def main():
    repo = InMemoryTaskRepository()

    create_task_uc = CreateTaskInteractor(repo)
    complete_task_uc = CompleteTaskInteractor(repo)
    list_tasks_uc = ListTasksInteractor(repo)

    controller = CLIController(
        create_task_uc=create_task_uc,
        complete_task_uc=complete_task_uc,
        list_tasks_uc=list_tasks_uc,
    )

    print("== Create tasks ==")
    t1 = controller.create_task("Make tea")
    t2 = controller.create_task("Check mail")

    print("\n== All tasks ==")
    controller.list_tasks()

    print("\n== Complete first task ==")
    controller.complete_task(t1.id)

    print("\n== All tasks ==")
    controller.list_tasks()


if __name__ == "__main__":
    main()
