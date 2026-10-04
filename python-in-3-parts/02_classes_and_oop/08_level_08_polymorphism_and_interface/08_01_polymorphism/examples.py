class CNN:
    def predict(self, x): return "CNN prediction"
class GNN:
    def predict(self, x): return "GNN prediction"
for model in [CNN(), GNN()]:
    print(model.predict("data"))
