from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@trace
def predict(x): return x * 2
print(predict(3))
print(predict.__name__)
