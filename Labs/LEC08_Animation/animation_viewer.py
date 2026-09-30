from pico2d import *

open_canvas(800, 800)

character = load_image('loopy_sprite_sheet.png')

frame = 0

clear_canvas()


w = character.w // 4
h = character.h // 4

character.clip_draw(
    frame * w, h * 3,
    w, h,
    400, 400,
    500, 500
)
update_canvas()

delay(3)
close_canvas()