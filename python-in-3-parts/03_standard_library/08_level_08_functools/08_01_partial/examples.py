from functools import partial

def power(x, exponent): return x ** exponent
square = partial(power, exponent=2)
print(square(5))
