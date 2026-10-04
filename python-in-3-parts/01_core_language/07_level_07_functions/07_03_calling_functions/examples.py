def predict(x):
    return x * 2
print(predict(5))

def train(epochs, lr):
    print(epochs, lr)
train(10, 0.001)
train(epochs=10, lr=0.001)

def train2(data, *, epochs=10):
    print(data, epochs)
train2("samples", epochs=20)

def f(a, b=10):
    print(a, b)
f(1); f(1, 20); f(a=1, b=30)

def add_item(values):
    values.append(100)
data = [1, 2]
add_item(data)
print(data)
