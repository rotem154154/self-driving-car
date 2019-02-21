import math

class Collision:
  def __init__(self):
    self.colx = 0
    self.coly = 0
  def lines_collision(self,x1,y1,x2,y2,x3,y3,x4,y4):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    x3 = float(x3)
    y3 = float(y3)
    x4 = float(x4)
    y4 = float(y4)

    if x1 > x2:
      x1,x2 = x2,x1
      y1,y2 = y2,y1
    if x3 > x4:
      x3,x4 = x4,x3
      y3,y4 = y4,y3
    d = ((x2 - x1) * (y4 - y3) - (y2-y1) * (x4-x3))
    num1 = ((y1-y3)*(x4 - x3) - (x1-x3)*(y4 - y3))
    num2 = ((y1-y3)*(x2-x1) - (x1-x3)*(y2-y1))
    if d == 0:
      return num1 == 0 and num2 == 0
    r = num1/d
    s = num2/d
    return (r >= 0 and r <= 1) and (s >= 0 and s <= 1)
  def lines_point(self,x1,y1,x2,y2,x3,y3,x4,y4):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    x3 = float(x3)
    y3 = float(y3)
    x4 = float(x4)
    y4 = float(y4)
    try:
      uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
      uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    except:
      return -1

    if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
      return (x1 + (uA * (x2 - x1)), y1 + (uA * (y2 - y1)))

    return -1



  def car_line_collision(self,car_points,x1,y1,x2,y2):
    r1 = self.lines_collision(car_points[0],car_points[1],car_points[2],car_points[3],x1,y1,x2,y2)
    r2 = self.lines_collision(car_points[2], car_points[3], car_points[4], car_points[5], x1, y1, x2, y2)
    r3 = self.lines_collision(car_points[4], car_points[5], car_points[6], car_points[7], x1, y1, x2, y2)
    r4 = self.lines_collision(car_points[6], car_points[7], car_points[0], car_points[1], x1, y1, x2, y2)
    if r1 or r2 or r3 or r4:
      return True
    return False

  def car_map_collision(self,car_points,car_map):
    for i in range(len(car_map.in_map)/2-1):
      if (self.car_line_collision(car_points,car_map.in_map[i*2],car_map.in_map[i*2+1],car_map.in_map[i*2+2],car_map.in_map[i*2+3])):
        return True
    if (self.car_line_collision(car_points, car_map.in_map[0], car_map.in_map[1], car_map.in_map[len(car_map.in_map)-2], car_map.in_map[len(car_map.in_map)-1])):
      return True
    for i in range(len(car_map.out_map)/2-1):
      if (self.car_line_collision(car_points,car_map.out_map[i*2],car_map.out_map[i*2+1],car_map.out_map[i*2+2],car_map.out_map[i*2+3])):
        return True
    if (self.car_line_collision(car_points, car_map.out_map[0], car_map.out_map[1], car_map.out_map[len(car_map.out_map)-2], car_map.out_map[len(car_map.out_map)-1])):
      return True
    return False



def dis(x1,y1,x2,y2):
  return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))