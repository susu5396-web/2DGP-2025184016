from pico2d import *

open_canvas(800, 800)

character = load_image('loopy_sprite_sheet.png')

w = character.w // 4
h = character.h // 4
frame = 0

for x in range(550, 250, -15):
    clear_canvas()

    character.clip_composite_draw(
        frame * w, h * 3 - 10,
        w, h + 10,
        0, 'h',
        x, 400,
        500, 500
    )

    update_canvas()

    frame = (frame + 1) % 4
    delay(0.15)

delay(1)

frame = 0

for count in range(4):
    clear_canvas()

    character.clip_composite_draw(
        frame * w, h + 10 ,
        w, h - 20,
        0, 'h',
        x, 400,
        500, 500
    )

    update_canvas()

    frame = (frame + 1) % 4
    delay(0.15)

# 점프 완료 후 1초 정지
delay(1)

close_canvas()