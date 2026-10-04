def add_value(x, values=None):
    if values is None:
        values = []
    values.append(x)
    return values
print(add_value(1))
print(add_value(2))

def report(*values, **options):
    print(values)
    print(options)
report(1, 2, 3, unit="mg")
