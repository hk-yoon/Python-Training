class Encoder:
    def encode(self, x): return x * 2
class Head:
    def predict(self, h): return h + 1
class Model:
    def __init__(self): self.encoder, self.head = Encoder(), Head()
    def predict(self, x): return self.head.predict(self.encoder.encode(x))
print(Model().predict(3))
