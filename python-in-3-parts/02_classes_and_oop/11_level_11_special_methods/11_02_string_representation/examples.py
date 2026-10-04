class Molecule:
    def __init__(self, name): self.name = name
    def __repr__(self): return f"Molecule(name={self.name!r})"
    def __str__(self): return self.name
m = Molecule("ATP")
print(repr(m))
print(str(m))
