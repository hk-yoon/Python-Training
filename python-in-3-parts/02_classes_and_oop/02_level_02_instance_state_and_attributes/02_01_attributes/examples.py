class Molecule:
    pass
m = Molecule()
m.name = "caffeine"
print(m.name)

class Molecule2:
    def __init__(self, name):
        self.name = name
m1 = Molecule2("ATP"); m2 = Molecule2("glucose")
print(m1.name, m2.name)

class Sample:
    def __init__(self, value): self.value = value
s = Sample(10)
s.value = 20
print(s.value)
