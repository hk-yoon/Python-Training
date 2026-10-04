class Temperature:
    def __init__(self, celsius): self.celsius = celsius
    def fahrenheit(self): return self.celsius * 9 / 5 + 32
print(Temperature(25).fahrenheit())

class Model:
    def predict(self, x): return x * 2
print(Model().predict(5))
