sample = {"id": "S01", "age": 40}
print("age" in sample)

sample = {"gene": "TP53"}
print(sample["gene"])

sample = {"gene": "TP53", "score": 0.91}
for key, value in sample.items():
    print(key, value)
