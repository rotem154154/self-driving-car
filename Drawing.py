import pyglet


def draw_line(color,x1,y1,x2,y2):
  x1 = int(x1)
  y1 = int(y1)
  x2 = int(x2)
  y2 = int(y2)
  draw = pyglet.graphics.Batch()
  draw.add(2, pyglet.gl.GL_LINES, None, ('v2i', (x1,y1,x2,y2)), ('c4B', color * 2))
  draw.draw()