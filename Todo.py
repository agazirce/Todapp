from enum import Enum


class Status(Enum):
    CURRENT = "current"
    DONE = "done"


class Todo:
    id: int
    title: str
    description: str
    status: Status

    def __init__(self, todo_id: int, title: str, description: str, status: str):
        self.id = todo_id
        self.title = title
        self.description = description
        self.status = status
