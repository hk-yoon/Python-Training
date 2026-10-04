def evaluate(model, x):
    return model.predict(x)
class SimpleModel:
    def predict(self, x): return x * 2
print(evaluate(SimpleModel(), 3))

class Predictor:
    def predict(self, x):
        if not isinstance(x, float): raise TypeError("x must be float")
        return x * 2
print(Predictor().predict(1.5))
