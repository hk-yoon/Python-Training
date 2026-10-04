class Model:
    def __init__(self, name): self.name = name
class CNN(Model):
    def __init__(self, name, channels):
        super().__init__(name)
        self.channels = channels
m = CNN("cnn", 64)
print(m.name, m.channels)
