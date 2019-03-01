

class Keyboard_helper:
  def __init__(self):
    self.up = 0
    self.down = 0
    self.left = 0
    self.right = 0
  def key_press(self,symbol,car):
    print symbol
    if symbol == 65362 or symbol == 119:
      self.up = 1
    if symbol == 65364 or symbol == 115 or symbol == 32:
      self.down = 1
    if symbol == 65361 or symbol == 97:
      self.left = 1
    if symbol == 65363 or symbol == 100:
      self.right = 1
    if symbol == 65293:
      if car.player_play:
        car.player_play = False
      else:
        car.player_play = True

  def key_release(self,symbol):
    if symbol == 65362 or symbol == 119:
      self.up = 0
    if symbol == 65364 or symbol == 115 or symbol == 32:
      self.down = 0
    if symbol == 65361 or symbol == 97:
      self.left = 0
    if symbol == 65363 or symbol == 100:
      self.right = 0

  def ai_keys(self,ai_prediction):
    if ai_prediction[0] > 0:
      self.up = 1
    else:
      self.up = 0
    if ai_prediction[1] > 0:
      self.down = 1
    else:
      self.down = 0
    if ai_prediction[2] > 0:
      self.left = 1
    else:
      self.left = 0
    if ai_prediction[3] > 0:
      self.right = 1
    else:
      self.right = 0
