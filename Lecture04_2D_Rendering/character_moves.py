from math import radians

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
    for x in range(0, 800, 5):
        draw_boy(750 - x, 50)
    pass

def move_left():
    print("Move Left")
    for y in range(0, 800, 5):
        draw_boy(0, 50 + y)
    pass

def move_triangle_top():
    for x in range(50, 400, 5):
        draw_boy(x, 50 + (x - 50) * math.tan(math.radians(60)))
    pass

def move_triangle_right():
    for y in range(50, 800, 5):
        draw_boy(400 + y / math.tan(math.radians(60)), 600 - y)
    pass

def move_triangle_left():
    for x in range(50, 800, 5):
        draw_boy(800 - x, 0)
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

def move_triangle():
    print("Move Triangle")
    move_triangle_top()
    move_triangle_right()
    move_triangle_left()

    pass

while True:
    # move_circle()
    # move_rectangle()
    move_triangle()
    pass

close_canvas()
