class Circle:
    def __init__(self, radius): self.radius = radius
    @property
    def area(self): return 3.14159 * self.radius ** 2
print(Circle(2).area)

class Concentration:
    def __init__(self, value): self.value = value
    @property
    def value(self): return self._value
    @value.setter
    def value(self, x):
        if x < 0: raise ValueError("value must be non-negative")
        self._value = x
c = Concentration(2.5)
print(c.value)
