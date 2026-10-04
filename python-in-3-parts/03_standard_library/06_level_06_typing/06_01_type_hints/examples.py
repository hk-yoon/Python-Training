from typing import Optional, Callable, Protocol

def mean(values: list[float]) -> float:
    return sum(values) / len(values)
print(mean([1.0, 2.0, 3.0]))

def find_gene(name: str) -> Optional[str]:
    return "found" if name == "TP53" else None
print(find_gene("TP53"))

def apply(f: Callable[[float], float], x: float) -> float:
    return f(x)
print(apply(lambda x: x * 2, 3.0))

class Predictor(Protocol):
    def predict(self, x: float) -> float: ...
class DoubleModel:
    def predict(self, x: float) -> float: return 2 * x
def evaluate(model: Predictor, x: float): return model.predict(x)
print(evaluate(DoubleModel(), 3.0))
