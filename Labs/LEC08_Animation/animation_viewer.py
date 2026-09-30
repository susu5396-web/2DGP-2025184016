from pico2d import *

open_canvas(800, 800)

character = load_image('loopy_sprite_sheet.png')

w = character.w // 4
h = character.h // 4

frame = 0

for count in range(4):
    clear_canvas()

    character.clip_draw(
        frame * w, h * 3 - 10,
        w, h + 10,
        400, 400,
        500, 500
    )

    update_canvas()
    delay(0.4)

    frame = (frame + 1) % 4

close_canvas()