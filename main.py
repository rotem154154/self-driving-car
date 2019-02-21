import pyglet
from Car import Car
from Car_Map import CarMap
from Collision import Collision
from Keyboard_helper import Keyboard_helper
import math
from pyglet.window import mouse

red = [255, 0, 0, 0]
green = [0, 255, 0, 0]
window = pyglet.window.Window(width=800,height=600)

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
    else:
        car.red_bool = False


@window.event
def on_draw():
    pyglet.gl.glClearColor(0,0,0,0)
    window.clear()
    pyglet.gl.glClearColor(0, 50, 0, 0)
    map.draw()
    car.draw()

map = CarMap()

car = Car()
keys = Keyboard_helper()
collision = Collision()
pyglet.clock.schedule_interval(update_frames,1/60.0)
pyglet.app.run()