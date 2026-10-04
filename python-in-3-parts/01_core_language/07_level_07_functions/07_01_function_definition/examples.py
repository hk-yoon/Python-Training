def square(x):
    return x * x
print(square(4))

def normalize(x):
    return x / 100
print(normalize(50))

def subtract(a, b):
    return a - b
print(subtract(10, 3))

def train(epochs, lr):
    print(epochs, lr)
train(lr=0.001, epochs=20)

def divide(x, y, /):
    return x / y
print(divide(10, 2))

def mean(*values):
    return sum(values) / len(values)
print(mean(1, 2, 3, 4))

def show_config(**config):
    print(config)
show_config(lr=0.001, epochs=20)

def f(a, /, b, *, c):
    print(a, b, c)
f(1, 2, c=3)
