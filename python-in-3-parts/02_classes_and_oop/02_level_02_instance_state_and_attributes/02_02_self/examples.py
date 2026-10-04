class Molecule:
    def show(self):
        print(self)
m = Molecule(); m.show()

class Molecule2:
    def __init__(self, name): self.name = name
    def show_name(self): print(self.name)
m = Molecule2("glucose"); m.show_name()
