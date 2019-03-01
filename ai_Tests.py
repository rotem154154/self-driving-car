from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
from numpy.random import randn
import torch.optim as optim
from torchvision import datasets, transforms


class Net(nn.Module):
  def __init__(self):
    super(Net, self).__init__()
    self.fc1 = nn.Linear(13, 8)
    self.fc2 = nn.Linear(8, 6)
    self.out = nn.Linear(6,4)
    self.fc1.double()
    self.fc2.double()
    self.out.double()

  def forward(self, x):

    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.out(x)
    # return F.log_softmax(x, dim=2)
    return x

  def change_weights(self,pre):
    self.fc1.weight.data += ((torch.rand(self.fc1.weight.data.size())-0.5) * pre).double()
    self.fc2.weight.data += ((torch.rand(self.fc2.weight.data.size()) - 0.5) * pre).double()
    self.out.weight.data += ((torch.rand(self.out.weight.data.size()) - 0.5) * pre).double()

