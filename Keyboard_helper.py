


class Keyboard_helper:
  def __init__(self):
    self.up = 0
    self.down = 0
    self.left = 0
    self.right = 0
  def key_press(self,symbol):
    if symbol == 65362 or symbol == 119:
      self.up = 1
    if symbol == 65364 or symbol == 115:
      self.down = 1
    if symbol == 65361 or symbol == 97:
      self.left = 1
    if symbol == 65363 or symbol == 100:
      self.right = 1
  def key_release(self,symbol):
    if symbol == 65362 or symbol == 119:
      self.up = 0
    if symbol == 65364 or symbol == 115:
      self.down = 0
    if symbol == 65361 or symbol == 97:
      self.left = 0
    if symbol == 65363 or symbol == 100:
      self.right = 0
