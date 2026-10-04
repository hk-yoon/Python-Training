import time
start = time.perf_counter()
total = sum(range(1_000_000))
print(total)
print(time.perf_counter() - start)
