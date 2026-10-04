class ModelA:
    def predict(self, x): return x + 1
class ModelB:
    def predict(self, x): return x * 2
def run(model, x): return model.predict(x)
print(run(ModelA(), 5))
print(run(ModelB(), 5))
