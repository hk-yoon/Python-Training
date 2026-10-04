class Encoder:
    def encode(self, x): return x * 2
class Model:
    def __init__(self): self.encoder = Encoder()
    def predict(self, x): return self.encoder.encode(x)
print(Model().predict(5))

class Encoder2: pass
class Model2:
    def __init__(self): self.encoder = Encoder2()
print(Model2().encoder)
