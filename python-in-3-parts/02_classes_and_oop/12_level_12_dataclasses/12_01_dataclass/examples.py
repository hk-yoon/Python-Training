from dataclasses import dataclass

@dataclass
class Sample:
    sample_id: str
    value: float
print(Sample("S01", 3.5))

@dataclass
class TrainConfig:
    batch_size: int
    learning_rate: float
config = TrainConfig(32, 0.001)
print(config.learning_rate)
