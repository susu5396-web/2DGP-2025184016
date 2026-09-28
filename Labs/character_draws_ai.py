import math
from pico2d import *

open_canvas(800, 600)
character = load_image('LEC06/character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.03)


def move_circle():
    for degree in range(0, 361, 2):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)

while True:
    move_circle()