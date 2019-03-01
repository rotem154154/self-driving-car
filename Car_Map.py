import pyglet

class CarMap:
  def __init__(self):
    self.in_map = [341, 161, 452, 121, 567, 123, 650, 160, 678, 241, 613, 340, 654, 467, 611, 508, 506, 514, 416, 437,
                   289, 401, 207, 431, 130, 469, 110, 424, 128, 320, 157, 229, 95, 99, 217, 87]
    self.out_map = [344, 89, 445, 45, 572, 59, 691, 92, 756, 229, 695, 333, 715, 482, 649, 566, 455, 567, 409, 502, 319,
                    476, 214, 492, 125, 550, 78, 557, 45, 485, 41, 353, 87, 254, 38, 88, 74, 35, 271, 44, 295, 70]
    self.score_lines = [341, 161,344, 89,567, 123,572, 59,678, 241,756, 229,654, 467,715, 482,506, 514,455, 567,130, 469,125, 550,157, 229,87, 254,95, 99,74, 35]
    #self.score_lines = [654, 467,715, 482,506, 514,455, 567,416,437,409,502,289,401,319,476,207,431,214,492,130, 469,125, 550,157, 229,87, 254,95, 99,74, 35]
    self.in_batch = pyglet.graphics.Batch()
    self.out_batch = pyglet.graphics.Batch()
    self.in_grey = [160] * (len(self.in_map) / 2)
    self.out_grey = [160] * (len(self.out_map) / 2)
    self.blue1 = [0, 39, 102,1]*(len(self.score_lines)/2)
    self.blue2 = [0, 97, 255, 1] * (2)
    self.in_batch.add(len(self.in_map) / 2, pyglet.gl.GL_LINE_LOOP, None, ('v2i', self.in_map),
                      ('c4B', self.in_grey * 4))
    self.out_batch.add(len(self.out_map) / 2, pyglet.gl.GL_LINE_LOOP, None, ('v2i', self.out_map),
                       ('c4B', self.out_grey * 4))

  def draw(self,score_activate):
    self.in_batch.draw()
    self.out_batch.draw()
    score_batch = pyglet.graphics.Batch()
    score_batch.add(16,pyglet.gl.GL_LINES,None,('v2i',self.score_lines),('c4B',self.blue1))
    score_batch.draw()
    score_batch2 = pyglet.graphics.Batch()
    score_batch2.add(2, pyglet.gl.GL_LINES, None, ('v2i', self.score_points(score_activate)), ('c4B', self.blue2))
    score_batch2.draw()

  def score_points(self,score_activate):
    if score_activate == 7:
      score_activate = -1
    return self.score_lines[score_activate*4+4:score_activate*4+8]
