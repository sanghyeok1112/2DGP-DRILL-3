from pico2d import *

open_canvas()
boy = load_image('character.png')
grass = load_image('grass.png')

def move_rectangle():
    print("Move Rectangle")
    pass

def move_circle():
    print("Move Circle")
    clear_canvas_now()
    boy_draw_now(400, 300)
    pass

while True:
    move_circle()
    move_rectangle()
    break
    pass

close_canvas()
