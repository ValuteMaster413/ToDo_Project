import datetime
from dataclasses import dataclass, field

@dataclass
class Task():
    id: int = None
    title: str =  None
    done: bool = False
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def mark_done(self) -> None:
        self.done =  True

    def mark_undone(self)-> None:
        self.done =  False

    def change_title(self, new_title: str) -> None:
        if not new_title or not new_title.strip():  
            raise ValueError("Title cannot be empty")
        
        self.title = new_title

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")

        if self.created_at is None:
            self.created_at = datetime.datetime.now()
            
        if self.done is None:
            self.done = False

    