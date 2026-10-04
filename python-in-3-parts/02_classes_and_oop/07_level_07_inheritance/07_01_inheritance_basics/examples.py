class Molecule:
    def describe(self): return "molecule"
class Protein(Molecule):
    pass
print(Protein().describe())

class BiologicalObject: pass
class Protein2(BiologicalObject): pass
print(isinstance(Protein2(), BiologicalObject))
