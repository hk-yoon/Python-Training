from concurrent.futures import ThreadPoolExecutor

def square(x): return x * x
with ThreadPoolExecutor() as executor:
    results = list(executor.map(square, [1, 2, 3, 4]))
print(results)
