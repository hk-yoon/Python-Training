import json

data = {"model": "CNN", "epochs": 20}
text = json.dumps(data)
print(text)

config = {"batch_size": 32, "learning_rate": 0.001}
print(json.dumps(config, indent=2))

text = '{"epochs": 30, "batch_size": 64}'
config = json.loads(text)
print(config["epochs"])

config = {"epochs": 10, "lr": 0.001}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)
with open("config.json", encoding="utf-8") as f:
    print(json.load(f))
