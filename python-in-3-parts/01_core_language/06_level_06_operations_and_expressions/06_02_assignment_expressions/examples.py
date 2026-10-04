values = [1, 2, 3]
if (n := len(values)) > 2:
    print(n)

text = "ATGC"
if (n := len(text)) > 3:
    print(n)

values = iter([3, 2, 1, 0])
while (x := next(values)) != 0:
    print(x)

values = [1, 2, 3, 4]
result = [y for x in values if (y := x * x) > 5]
print(result)
