score = 0.85
if score >= 0.8:
    print("high")
else:
    print("low")

score = 0.9
label = "positive" if score > 0.5 else "negative"
print(label)

data = None
if data is not None and len(data) > 0:
    print("has data")
else:
    print("no data")

x = 0.7
if 0.0 <= x <= 1.0:
    print("valid probability")
