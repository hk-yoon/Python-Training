import random, json
seed = 42
random.seed(seed)
metadata = {"seed": seed, "model": "CNN"}
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)
print(metadata)
