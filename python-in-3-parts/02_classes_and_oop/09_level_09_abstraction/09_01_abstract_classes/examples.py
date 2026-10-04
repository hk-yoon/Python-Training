from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def predict(self, x):
        pass

class LinearModel(Model):
    def predict(self, x): return 2 * x
print(LinearModel().predict(3))
