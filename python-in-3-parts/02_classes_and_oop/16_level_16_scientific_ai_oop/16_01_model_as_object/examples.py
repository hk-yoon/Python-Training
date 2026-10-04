class LinearModel:
    def __init__(self, weight): self.weight = weight
    def predict(self, x): return self.weight * x
model = LinearModel(2.0)
print(model.predict(3.0))
