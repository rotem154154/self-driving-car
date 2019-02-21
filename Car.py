import pyglet
import math

class Car:
  def __init__(self):
    self.score = 0
    self.last_score = 7
    self.red_bool = False
    self.x = 440.0
    self.y = 90.0
    self.rotation = math.pi/2
    self.v = 0.05
    self.speed = 0.05
    self.sizex = 16.0
    self.sizey = 32.0
    self.size_radius = math.sqrt(self.sizex*self.sizex+self.sizey*self.sizey)
    self.size_rotation = math.atan(self.sizey/self.sizex)
    self.red = [255, 0, 0]
    self.white = [255, 255, 255]

  def get_points(self):
    x1_rot = math.pi + self.size_rotation + self.rotation
    x2_rot = math.pi - self.size_rotation + self.rotation
    x3_rot = self.size_rotation + self.rotation
    x4_rot = -self.size_rotation + self.rotation

    x1 = int(self.x + math.cos(x1_rot+math.pi/2)*(self.size_radius / 2))
    x2 = int(self.x + math.cos(x2_rot+math.pi/2)*(self.size_radius / 2))
    x3 = int(self.x + math.cos(x3_rot+math.pi/2)*(self.size_radius / 2))
    x4 = int(self.x + math.cos(x4_rot+math.pi/2)*(self.size_radius / 2))
    y1 = int(self.y + math.sin(x1_rot+math.pi/2)*(self.size_radius / 2))
    y2 = int(self.y + math.sin(x2_rot+math.pi/2)*(self.size_radius / 2))
    y3 = int(self.y + math.sin(x3_rot+math.pi/2)*(self.size_radius / 2))
    y4 = int(self.y + math.sin(x4_rot+math.pi/2)*(self.size_radius / 2))
    return (x1, y1, x2, y2, x3, y3, x4, y4)

  def draw(self):
    if self.red_bool:
      quad = pyglet.graphics.vertex_list(4, ('v2i', self.get_points()), ('c3B', self.red * 4))
    else:
      quad = pyglet.graphics.vertex_list(4, ('v2i', self.get_points()), ('c3B', self.white * 4))
    quad.draw(pyglet.gl.GL_QUADS)

  def update(self,keys):
    if keys.left == 1:
      self.rotation+=0.07
      # self.car_brake(0.1)
    if keys.right == 1:
      self.rotation -= 0.07
      # self.car_brake(0.1)
    if keys.up == 1:
      self.v += self.speed
    if keys.down == 1:
      self.v -= self.speed*3
    self.x += math.cos(self.rotation)*self.v
    self.y += math.sin(self.rotation)*self.v
    self.car_brake(0.005)

  def car_brake(self,brake):
    self.v = max(self.v - brake,0)
