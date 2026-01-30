import torch
import torch.nn as nn

relu = nn.ReLU()

x = torch.tensor([-3.0, -1.0, 0.0, 2.0, 5.0])
y = relu(x)

print(y)  # tensor([0., 0., 0., 2., 5.])