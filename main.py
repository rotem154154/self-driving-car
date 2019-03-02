#   To play yourself click enter
#   To train car models click with the mouse
#   You can move the car with the arrows and brake with space
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
import glob, os
import random

#   change car model
car_model = 'i7437'


glob_frame = 0
saved_car_count = 0
red = [255, 0, 0, 0]
green = [0, 255, 0, 0]
window = pyglet.window.Window(width=800,height=600)
label = pyglet.text.Label(str(0),
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2 + 30,
                          anchor_x='center', anchor_y='center')
label2 = pyglet.text.Label(str(0),
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2 - 30,
                          anchor_x='center', anchor_y='center')


def ai_game(frames, ai, net, in_map, out_map):
    global car

    car = Car()
    best_score = 0
    for i in range(frames):
        f = car.rays(ai, net, in_map, out_map, False)
        keys.ai_keys(f)
        update_frames(1)
        best_score = max(car.score,best_score)

    return (best_score + car.score)/2

def net_tests(num_nets,algo):
    global net
    global saved_car_count
    os.chdir("models")
    models = glob.glob("*.txt")
    for i in range(num_nets):
        net = Net()
        if algo == 1:
            m1 = random.choice(models)
            # m1 = models[0]
            net.load_state_dict(torch.load(m1, map_location=device))
            net.change_weights(random.uniform(0,1))
        net.double()
        score = ai_game(120 + saved_car_count*3, ai, net, map.in_map, map.out_map)
        need_to_save = 1000 + 10 * saved_car_count
        # print score
        #  you can decide minimum score to save the model
        if True and score > need_to_save:
            name = 'g' + str(score) + '.txt'
            torch.save(net.state_dict(), name)
            models.append(name)
            # print score
            saved_car_count+=1
            print saved_car_count,i,score,need_to_save






@window.event
def on_mouse_press(x, y, button, modifiers):
    # print(net.forward(torch.zeros(13)))
    net_tests(2,algo=0)
    net_tests(2,algo=1)


@window.event
def on_key_press(symbol, modifiers):
    keys.key_press(symbol,car)

@window.event
def on_key_release(symbol, modifiers):
    keys.key_release(symbol)

def update_frames(dt):
    car.update(keys)
    if collision.car_map_collision(car.get_points(),map):
        car.red_bool = True
        car.score -= 10 + saved_car_count
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
    global glob_frame
    glob_frame+=1
    label2.text = str(glob_frame)
    label2.draw()
    if not car.player_play:
        f = car.rays(ai,net,map.in_map,map.out_map,True)
        keys.ai_keys(f)
    # print f
    fps_display.draw()



fps_display = FPSDisplay(window)

map = CarMap()
ai = Ai()
net = Net()
device = torch.device('cpu')
net.load_state_dict(torch.load('models/'+car_model+'.txt', map_location=device))
net.double()
car = Car()
keys = Keyboard_helper()
collision = Collision()
pyglet.clock.schedule_interval(update_frames,1/24.0)
pyglet.app.run()

