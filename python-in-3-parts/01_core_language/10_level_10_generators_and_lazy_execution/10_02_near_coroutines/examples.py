def receiver():
    value = yield
    print("received:", value)

g = receiver()
next(g)
g.send(42)
