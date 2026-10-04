class Molecule:
    category = "chemical"
m1 = Molecule(); m2 = Molecule()
print(m1.category, m2.category)

class Molecule2:
    category = "chemical"
    def __init__(self, name): self.name = name
m = Molecule2("ATP")
print(m.name, m.category)
