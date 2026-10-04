class Encoder:
    def encode(self, x): return x * 2
class Model:
    def __init__(self, encoder): self.encoder = encoder
model = Model(Encoder())
print(model.encoder.encode(5))
