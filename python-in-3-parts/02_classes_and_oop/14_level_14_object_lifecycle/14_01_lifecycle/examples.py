class Sample:
    def __init__(self, name): self.name = name
s = Sample("S01")
print(s.name)
del s

import gc
print(gc.collect())
