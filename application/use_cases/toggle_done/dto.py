from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ToggleDoneCommand:
    id: str  

@dataclass(frozen=True)
class ToggleDoneResult:
    id: str
    completed: bool
