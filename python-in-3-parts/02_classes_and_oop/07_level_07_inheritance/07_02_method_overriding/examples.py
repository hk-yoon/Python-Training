class Model:
    def predict(self, x): return x
class DoubleModel(Model):
    def predict(self, x): return x * 2
print(DoubleModel().predict(5))
