import random
print(random.random())
print(random.randint(1, 10))
print(random.choice(["A", "T", "G", "C"]))
samples = ["S1", "S2", "S3", "S4"]
random.shuffle(samples)
print(samples)
random.seed(42)
print(random.random())
