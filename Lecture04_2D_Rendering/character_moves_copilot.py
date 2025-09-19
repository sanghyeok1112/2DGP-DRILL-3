from pico2d import *
import math

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def move_top():
    for x in range(0, 800, 5):
        draw_boy(x, 550)

def move_right():
    for y in range(0, 520, 5):
        draw_boy(800, 550 - y)

def move_bottom():
    for x in range(800, 0, -5):
        draw_boy(x, 30 + 90)

def move_left():
    for y in range(0, 520, 5):
        draw_boy(0, 120 + y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_circle():
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)

while True:
    move_rectangle()
    move_circle()

close_canvas()

