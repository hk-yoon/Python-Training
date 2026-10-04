try:
    import torch
    from torch import nn
except ImportError:
    raise SystemExit("This example requires PyTorch: pip install torch")

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 1)
    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
x = torch.randn(2, 3)
print(model(x).shape)
