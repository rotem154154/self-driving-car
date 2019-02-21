import pyglet

class CarMap:
  def __init__(self):
    self.in_map = [341, 161, 452, 121, 567, 123, 650, 160, 678, 241, 613, 340, 654, 467, 611, 508, 506, 514, 416, 437,
                   289, 401, 207, 431, 130, 469, 110, 424, 128, 320, 157, 229, 95, 99, 217, 87]
    self.out_map = [344, 89, 445, 45, 572, 59, 691, 92, 756, 229, 695, 333, 715, 482, 649, 566, 455, 567, 409, 502, 319,
                    476, 214, 492, 125, 550, 78, 557, 45, 485, 41, 353, 87, 254, 38, 88, 74, 35, 271, 44, 295, 70]
    self.in_batch = pyglet.graphics.Batch()
    self.out_batch = pyglet.graphics.Batch()
    self.in_grey = [160] * (len(self.in_map) / 2)
    self.out_grey = [160] * (len(self.out_map) / 2)
    self.in_batch.add(len(self.in_map) / 2, pyglet.gl.GL_LINE_LOOP, None, ('v2i', self.in_map),
                      ('c4B', self.in_grey * 4))
    self.out_batch.add(len(self.out_map) / 2, pyglet.gl.GL_LINE_LOOP, None, ('v2i', self.out_map),
                       ('c4B', self.out_grey * 4))

  def draw(self):
    self.in_batch.draw()
    self.out_batch.draw()