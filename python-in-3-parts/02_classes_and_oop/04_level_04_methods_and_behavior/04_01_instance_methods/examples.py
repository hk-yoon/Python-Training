class Molecule:
    def describe(self): return "A molecule"
m = Molecule(); print(m.describe())

class Sample:
    def __init__(self, value): self.value = value
    def double(self): self.value *= 2
s = Sample(10); s.double(); print(s.value)

class Cell:
    def __init__(self, count): self.count = count
    def divide(self): self.count *= 2
cell = Cell(10); cell.divide(); print(cell.count)
