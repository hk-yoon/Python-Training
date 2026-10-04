class Trainable: pass
class Serializable: pass
class Model(Trainable, Serializable): pass
m = Model()
print(isinstance(m, Trainable))

class A: pass
class B(A): pass
class C(B): pass
print(C.mro())
