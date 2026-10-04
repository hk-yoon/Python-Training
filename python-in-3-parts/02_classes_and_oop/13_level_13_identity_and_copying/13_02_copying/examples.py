import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0].append(99)
print(a)

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
print(a)
print(b)
