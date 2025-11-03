from datetime import datetime, timezone
from dataclasses import dataclass, field
from domain.value_objects.task_id import TaskId

@dataclass
class Task():
    id: TaskId
    title: str =  None
    done: bool = False
    created_at: datetime = datetime.now(timezone.utc)

    def mark_done(self) -> None:
        self.done =  True

    def mark_undone(self)-> None:
        self.done =  False

    def change_title(self, new_title: str) -> None:
        if not new_title or not new_title.strip():  
            raise ValueError("Title cannot be empty")
        
        self.title = new_title

    