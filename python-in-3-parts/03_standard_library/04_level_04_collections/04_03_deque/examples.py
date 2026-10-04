from collections import deque
queue = deque(["A", "B"])
queue.append("C")
print(queue.popleft())
print(queue)
