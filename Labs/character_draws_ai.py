from pico2d import *

open_canvas(800, 600)
character = load_image('LEC06/character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.03)


while True:
    draw_character(400, 300)