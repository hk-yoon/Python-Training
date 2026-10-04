class CNNEncoder:
    def encode(self, x): return f"CNN({x})"
class TransformerEncoder:
    def encode(self, x): return f"Transformer({x})"
class Model:
    def __init__(self, encoder): self.encoder = encoder
    def predict(self, x): return self.encoder.encode(x)
print(Model(CNNEncoder()).predict("data"))
print(Model(TransformerEncoder()).predict("data"))
