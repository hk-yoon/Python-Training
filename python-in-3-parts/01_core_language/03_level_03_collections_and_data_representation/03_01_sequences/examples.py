values = [10, 20, 30]
print(values[1])

sequence = "ATGC"
print(sequence[0])
print(sequence[1:3])

data = b"ABC"
print(data, data[0])

mutable_data = bytearray(b"ABC")
mutable_data[0] = 90
print(mutable_data)

shape = (32, 3, 224, 224)
print(shape[0])

samples = ["A", "B"]
samples.append("C")
print(samples)
