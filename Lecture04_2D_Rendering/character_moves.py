from pico2d import *
import math

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')

def move_rectangle():
    print("Move Rectangle")
    pass

def move_circle():
    print("Move Circle")
    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300

        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.01)

    pass

while True:
    move_circle()
    move_rectangle()
    break
    pass

close_canvas()
