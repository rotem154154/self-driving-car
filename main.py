import pyglet
from pyglet.window import FPSDisplay
from Car import Car
from Car_Map import CarMap
from Collision import Collision
from Keyboard_helper import Keyboard_helper
from ai import Ai
from ai_Tests import Net
import math
import torch
from pyglet.window import mouse

red = [255, 0, 0, 0]
green = [0, 255, 0, 0]
window = pyglet.window.Window(width=800,height=600)
label = pyglet.text.Label(str(0),
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


def ai_game(frames, ai, net, in_map, out_map):
    global car
    car = Car()
    for i in range(frames):
        f = car.rays(ai, net, in_map, out_map, False)
        keys.ai_keys(f)
        update_frames(1)

    return car.score

def net_tests(num_nets):
    global net
    nets = []
    for i in range(num_nets):
        net = Net()
        net.double()
        score = ai_game(1000, ai, net, map.in_map, map.out_map)
        nets.append([score,net])
        print(i,score)
    nets.sort(key=lambda tup: tup[0])
    nets.reverse()
    torch.save(nets[0][1].state_dict(), 'models/'+str(nets[0][0])+'.txt')




@window.event
def on_mouse_press(x, y, button, modifiers):
    # print(net.forward(torch.zeros(13)))
    net_tests(14)


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
    f = car.rays(ai,net,map.in_map,map.out_map,False)
    keys.ai_keys(f)
    print f
    fps_display.draw()


fps_display = FPSDisplay(window)

map = CarMap()
ai = Ai()
net = Net()
device = torch.device('cpu')
net.load_state_dict(torch.load('models/-230.txt', map_location=device))
net.double()
car = Car()
keys = Keyboard_helper()
collision = Collision()
pyglet.clock.schedule_interval(update_frames,1/24.0)
pyglet.app.run()

