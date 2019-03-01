import pyglet
import math
import Drawing
import Collision
import numpy as np
import torch


class Car:
  def __init__(self):
    self.player_play = False
    self.score = 0
    self.last_score = 7
    self.red_bool = False
    self.x = 440.0
    self.y = 90.0
    #self.x = 570.0
    #self.y = 540.0

    self.rotation = 0
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

  def rays(self,ai,net,in_map,out_map,draw):
    points = self.get_points()
    dists = np.zeros(13)
    for i in range(6):
      dists[i] = self.ray_map(draw,points[0],points[1],-(i)*math.pi/10,in_map,out_map)
    for i in range(6):
      dists[i+6] = self.ray_map(draw, points[6], points[7], (i) * math.pi / 10, in_map, out_map)
    dists[12] = self.v
    fixed = ai.new_input(dists)

    f = net.forward(torch.from_numpy(fixed))
    return f


    # x1,y1,x2,y2 = 301,400,300,300
    # Drawing.draw_line([255,255,0,1],x1,y1,x2,y2)
    # x,y,dis = self.ray_line(points[0],points[1],x1,y1,x2,y2)
    # if dis != -1:
    #   Drawing.draw_line([0,255,0,1],points[0],points[1],x,y)

  def ray_map(self,draw_ray,start_x,start_y,alpha,in_map,out_map):
    smallest_dis,smallest_x,smallest_y = 1000.0,0.0,0.0
    ray_x1,ray_y1,ray_x2,ray_y2 = 100,100,300,300
    for i in range(len(in_map)/2-1):
      x,y,dis = self.ray_line(start_x, start_y,alpha, in_map[i * 2], in_map[i * 2 + 1], in_map[i * 2 + 2], in_map[i * 2 + 3])
      if dis != -1 and dis < smallest_dis:
        smallest_dis,smallest_x,smallest_y = dis,x,y
        ray_x1, ray_y1, ray_x2, ray_y2 = in_map[i * 2], in_map[i * 2 + 1], in_map[i * 2 + 2], in_map[i * 2 + 3]
    x,y,dis = self.ray_line(start_x, start_y,alpha, in_map[len(in_map)-2], in_map[len(in_map)-1], in_map[0],
                        in_map[1])
    if dis != -1 and dis < smallest_dis:
      smallest_dis, smallest_x, smallest_y = dis, x, y
      ray_x1, ray_y1, ray_x2, ray_y2 = in_map[i * 2], in_map[i * 2 + 1], in_map[i * 2 + 2], in_map[i * 2 + 3]

    for i in range(len(out_map)/2-1):
      x,y,dis = self.ray_line(start_x, start_y,alpha, out_map[i * 2], out_map[i * 2 + 1], out_map[i * 2 + 2], out_map[i * 2 + 3])
      if dis != -1 and dis < smallest_dis:
        smallest_dis,smallest_x,smallest_y = dis,x,y
        ray_x1, ray_y1, ray_x2, ray_y2 = out_map[i * 2], out_map[i * 2 + 1], out_map[i * 2 + 2], out_map[i * 2 + 3]
    x,y,dis = self.ray_line(start_x, start_y,alpha, out_map[len(out_map)-2], out_map[len(out_map)-1], out_map[0],
                        out_map[1])
    if dis != -1 and dis < smallest_dis:
      smallest_dis, smallest_x, smallest_y = dis, x, y
      ray_x1, ray_y1, ray_x2, ray_y2 = out_map[i * 2], out_map[i * 2 + 1], out_map[i * 2 + 2], out_map[i * 2 + 3]

    if draw_ray and smallest_dis < 500:
      Drawing.draw_line([0,255,0,1],smallest_x,smallest_y,start_x,start_y)
    return smallest_dis

  def ray_line(self,start_x,start_y,alpha,x1,y1,x2,y2):
    x, y, dis = raycast(start_x, start_y, self.rotation + alpha, x1,y1,x2,y2)
    if x != -1 and y != -1:
      if abs(Collision.dis(x1,y1, x, y) + Collision.dis(x, y, x2,y2) - Collision.dis(x1,y1,x2,y2)) < 0.0001:
        return x,y,dis
    return -1,-1,-1


  def update(self,keys):
    if keys.left == 1:
      if (keys.down == 1):
        self.rotation += 0.07 * 2
      else:
        self.rotation += 0.07
    if keys.right == 1:
      if (keys.down == 1):
        self.rotation -= 0.07 * 2
      else:
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





def raycast(xt,yt,alpha,x1,y1,x2,y2):
  if x1 > x2:
    x1,x2 = x2,x1
    y1,y2 = y2,y1
  xt = float(xt)
  yt = float(yt)
  alpha = float(alpha)
  x1 = float(x1)
  y1 = float(y1)
  x2 = float(x2)
  y2 = float(y2)
  m = math.tan(alpha)
  m2 = (y2-y1)/(x2-x1)
  x = (m * xt - m2 * x1 + y1 - yt) / (m - m2)
  y = x * m2 - x2 * m2 + y2
  d = (xt-x1)*(y2-y1)-(yt-y1)*(x2-x1)
  a2 = math.atan(m2)
  ezer = round((alpha-a2+math.pi/2)/(math.pi))%2
  if (d >= 0 and ezer == 1) or (d < 0 and ezer == 0):
    return x, y, Collision.dis(x,y,xt,yt)
  return -1,-1,-1

