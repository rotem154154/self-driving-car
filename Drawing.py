import pyglet


def draw_line(points, color):
  draw = pyglet.graphics.Batch()
  draw.add(2, pyglet.gl.GL_LINES, None, ('v2i', points), ('c4B', color * 2))
  draw.draw()