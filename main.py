from infrastructure.mediator.di import build_default_mediator
from application.use_cases.create_task.dto import CreateTaskCommand
from application.use_cases.get_task_by_id.dto import GetTaskByIdQuery
from application.use_cases.list_tasks.dto import ListTasksQuery
from application.use_cases.toggle_done.dto import ToggleDoneCommand

def main() -> None:
    mediator = build_default_mediator()

    r1 = mediator.send(CreateTaskCommand(title="Read Clean Architecture"))
    r2 = mediator.send(CreateTaskCommand(title="Write tests"))
    print("Created:")
    print(" ", r1)
    print(" ", r2)

    found = mediator.send(GetTaskByIdQuery(id=r1.id))
    print("Found by id:", found)

    listing = mediator.send(ListTasksQuery())
    print("List:")
    for item in listing.items:
        print(" ", item)

    t1 = mediator.send(ToggleDoneCommand(id=r1.id))
    print("After toggle:", t1)

    t2 = mediator.send(ToggleDoneCommand(id=r1.id))
    print("After 2nd toggle:", t2)

if __name__ == "__main__":
    main()
