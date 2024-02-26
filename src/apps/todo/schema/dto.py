from dataclasses import dataclass


@dataclass
class TodoDto:
    title: str
    completed: bool
