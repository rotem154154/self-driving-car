import pyglet
from pyglet.window import FPSDisplay
from Car import Car
from Car_Map import CarMap
from Collision import Collision
from Keyboard_helper import Keyboard_helper
import math
from pyglet.window import mouse

red = [255, 0, 0, 0]
green = [0, 255, 0, 0]
window = pyglet.window.Window(width=800,height=600)
label = pyglet.text.Label(str(0),
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_mouse_press(x, y, button, modifiers):
    print 'mouse'

@window.event
def on_key_press(symbol, modifiers):
    keys.key_press(symbol)

@window.event
def on_key_release(symbol, modifiers):
    keys.key_release(symbol)

def update_frames(dt):
    car.update(keys)
    if collision.car_map_collision(car.get_points(),map):
        car.red_bool = True
        car.score -= 10
    else:
        car.red_bool = False

    score_points = map.score_points((car.last_score + 1) % 8)
    if collision.car_line_collision(car.get_points(),score_points[0],score_points[1],score_points[2],score_points[3]):
        car.score += 500
        car.last_score += 1

    car.score -= 1

@window.event
def on_draw():
    pyglet.gl.glClearColor(0,0,0,0)
    window.clear()
    pyglet.gl.glClearColor(0, 50, 0, 0)
    map.draw(score_activate=(car.last_score+1)%8)
    car.draw()
    label.text = str(car.score)
    label.draw()
    car.draw_ray(map.in_map,map.out_map)
    fps_display.draw()


fps_display = FPSDisplay(window)

map = CarMap()

car = Car()
keys = Keyboard_helper()
collision = Collision()
pyglet.clock.schedule_interval(update_frames,1/30.0)
pyglet.app.run()
