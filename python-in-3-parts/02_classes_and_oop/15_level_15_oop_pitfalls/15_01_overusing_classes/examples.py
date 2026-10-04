def normalize(x, mean, std):
    return (x - mean) / std
print(normalize(10, 5, 2))
