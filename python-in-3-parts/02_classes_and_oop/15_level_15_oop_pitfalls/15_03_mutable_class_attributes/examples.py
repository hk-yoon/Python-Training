class Sample:
    values = []
s1 = Sample(); s2 = Sample()
s1.values.append(10)
print(s2.values)

class SafeSample:
    def __init__(self): self.values = []
s1 = SafeSample(); s2 = SafeSample()
s1.values.append(10)
print(s1.values)
print(s2.values)
