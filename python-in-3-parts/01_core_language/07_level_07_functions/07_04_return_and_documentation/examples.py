def add(a, b):
    return a + b
print(add(2, 3))

def mean(values):
    """Return the arithmetic mean."""
    return sum(values) / len(values)
print(mean.__doc__)

def predict(x):
    """Simple prediction."""
    return x
print(predict.__name__)
print(predict.__doc__)
predict.version = "1.0"
print(predict.version)

def square(x: float) -> float:
    return x * x
print(square(3.0))
