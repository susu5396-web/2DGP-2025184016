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

def move_rectangle():
    for x in range(150, 651, 10):
        draw_character(x, 400)

    for y in range(400, 199, -10):
        draw_character(650, y)

    for x in range(650, 149, -10):
        draw_character(x, 200)

    for y in range(200, 401, 10):
        draw_character(150, y)

def move_triangle():
    # 왼쪽 아래 → 꼭대기
    x, y = 200, 150
    for z in range(51):
        draw_character(x, y)
        x += 4
        y += 6

    # 꼭대기 → 오른쪽 아래
    x, y = 400, 450
    for z in range(51):
        draw_character(x, y)
        x += 4
        y -= 6

    # 오른쪽 아래 → 왼쪽 아래
    x, y = 600, 150
    for z in range(51):
        draw_character(x, y)
        x -= 8

while True:
    move_circle()
    move_rectangle()
    move_triangle()