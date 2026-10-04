def numbers():
    yield 1
    yield 2
    yield 3
for x in numbers():
    print(x)

def all_numbers():
    yield from [1, 2, 3]
    yield from [4, 5]
print(list(all_numbers()))

squares = (x * x for x in range(5))
print(next(squares))
print(next(squares))
