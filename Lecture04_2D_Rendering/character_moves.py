from pico2d import *
import math

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def move_top():
    print('Move Top')
    for x in range(0, 800, 5):
        draw_boy(x, 550)
    pass

def move_right():
    print("Move Right")
    for y in range(0, 800, 5):
        draw_boy(800, 550 - y)
    pass

def move_bottom():
    print("Move Bottom")
    pass

def move_left():
    print("Move Left")
    pass


def move_rectangle():

    print("Move Rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_circle():
    print("Move Circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass

while True:
    # move_circle()
    move_rectangle()
    break
    pass

close_canvas()
