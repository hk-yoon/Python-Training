from dataclasses import dataclass
import json

@dataclass
class Config:
    batch_size: int
    learning_rate: float
text = '{"batch_size": 32, "learning_rate": 0.001}'
config = Config(**json.loads(text))
print(config)
