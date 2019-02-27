import numpy as np

class Ai:
  def __init__(self):
    self.input = np.zeros(13)

  def new_input(self,input):
    for i in range(12):
      self.input[i] = input[i] / 500
    self.input[12] = input[12] / 10
    return self.input