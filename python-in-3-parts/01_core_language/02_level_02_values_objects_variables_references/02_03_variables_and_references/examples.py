x = [1, 2, 3]
y = x
y.append(4)
print(x)

data = {"sample": [1, 2, 3]}
print(data["sample"])

text = "DNA"
print(text.lower())
print(text[0])

sample = {"id": 1}
try:
    print(sample["name"])
except KeyError as e:
    print("KeyError:", e)
