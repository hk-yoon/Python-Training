x = 10

def f():
    y = 20
    print(x, y)
f()

count = 0
def increment():
    global count
    count += 1
increment()
print(count)
