def outer(scale):
    def inner(x):
        return x * scale
    return inner

double = outer(2)
print(double(5))
