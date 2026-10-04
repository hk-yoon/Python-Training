class Encoder:
    def __call__(self, x): return x * 2
class Head:
    def __call__(self, x): return x + 1
class Model:
    def __init__(self, encoder, head): self.encoder, self.head = encoder, head
    def __call__(self, x): return self.head(self.encoder(x))
print(Model(Encoder(), Head())(10))
