import math
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x, y):
    for event in get_events():
        if event.type == SDL_QUIT:
            raise SystemExit
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            raise SystemExit

    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.03)