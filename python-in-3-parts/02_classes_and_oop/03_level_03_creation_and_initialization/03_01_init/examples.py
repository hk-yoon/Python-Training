class Molecule:
    def __init__(self, name): self.name = name
m = Molecule("aspirin")
print(m.name)

class Sample:
    def __init__(self, sample_id): self.sample_id = sample_id
s = Sample("S01")
print(s.sample_id)

class Experiment:
    def __init__(self, temperature=25.0): self.temperature = temperature
e = Experiment()
print(e.temperature)
