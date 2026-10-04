class Model:
    def __init__(self): self._state = "internal"
print(Model()._state)

class Model2:
    def __init__(self): self.__version = 1
m = Model2()
print(m._Model2__version)
