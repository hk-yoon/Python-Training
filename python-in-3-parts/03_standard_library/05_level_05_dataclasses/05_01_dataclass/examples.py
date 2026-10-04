from dataclasses import dataclass, field

@dataclass
class Sample:
    sample_id: str
    value: float
print(Sample("S01", 3.5))

@dataclass
class TrainConfig:
    batch_size: int = 32
    epochs: int = 20
print(TrainConfig())

@dataclass
class Experiment:
    results: list = field(default_factory=list)
e1, e2 = Experiment(), Experiment()
e1.results.append(1)
print(e1.results, e2.results)
