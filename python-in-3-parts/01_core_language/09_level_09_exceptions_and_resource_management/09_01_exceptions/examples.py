def normalize(x):
    if x == 0:
        raise ValueError("x must not be zero")

try:
    normalize(0)
except ValueError as e:
    print(e)
