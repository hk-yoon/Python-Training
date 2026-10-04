class Molecule:
    category = "chemical"
    @classmethod
    def show_category(cls): return cls.category
print(Molecule.show_category())

class Sample:
    def __init__(self, sample_id, value): self.sample_id, self.value = sample_id, value
    @classmethod
    def from_string(cls, text):
        sample_id, value = text.split(",")
        return cls(sample_id, float(value))
s = Sample.from_string("S01,3.5")
print(s.sample_id, s.value)
