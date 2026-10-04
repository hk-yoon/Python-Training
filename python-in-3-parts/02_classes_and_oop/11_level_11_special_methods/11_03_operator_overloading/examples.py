class Vector:
    def __init__(self, x): self.x = x
    def __add__(self, other): return Vector(self.x + other.x)
    def __repr__(self): return f"Vector({self.x})"
print(Vector(2) + Vector(3))
