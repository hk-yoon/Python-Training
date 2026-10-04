for base in "ATGC":
    print(base)

values = [10, 20, 30]
it = iter(values)
print(next(it))
print(next(it))

values = [1, 2, 3]
it = iter(values)
print(values)
print(next(it))

for i in range(5):
    print(i)
