from enum import Enum

command = "start"
match command:
    case "start": print("running")
    case "stop": print("stopped")

point = (10, 20)
match point:
    case (x, y): print(x, y)

status = 200
match status:
    case 200: print("OK")

value = 17
match value:
    case 0: print("zero")
    case _: print("other")

value = 42
match value:
    case x: print(x)

class Status(Enum):
    OK = 1
status = Status.OK
match status:
    case Status.OK: print("OK")

base = "A"
match base:
    case "A" | "G": print("purine")

point = [10, 20]
match point:
    case [x, y]: print(x, y)

point = (3, 4)
match point:
    case (x, y) as p: print(x, y, p)

sample = {"id": "S01", "value": 10}
match sample:
    case {"id": sample_id}: print(sample_id)

class Sample:
    def __init__(self, value): self.value = value
sample = Sample(10)
match sample:
    case Sample(value=x): print(x)

point = (10, 20)
match point:
    case (x, y) if x < y: print("x < y")

class Point:
    __match_args__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y
p = Point(1, 2)
match p:
    case Point(x, y): print(x, y)
