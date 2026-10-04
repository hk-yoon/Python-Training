from enum import Enum
class Status(Enum):
    READY = 1
    RUNNING = 2
    DONE = 3
print(Status.READY)
