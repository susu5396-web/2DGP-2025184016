from pathlib import Path

from pico2d import (
    SDL_QUIT,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SPRITE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
FRAME_SCALE = 6
FRAME_DELAY = 0.1
ANIMATION_REPEAT_COUNT = 5
ANIMATION_PAUSE = 1.0
ANIMATION_FRAME_BOXES = (
    (
        (1, 39, 30, 78), (31, 40, 57, 78), (58, 39, 86, 78),
        (86, 40, 116, 78), (118, 40, 148, 78), (150, 40, 180, 78),
        (182, 40, 211, 78), (211, 39, 240, 77), (240, 39, 269, 77),
        (270, 45, 294, 77), (302, 51, 331, 77),
    ),
    (
        (8, 80, 34, 117), (37, 80, 64, 117), (65, 80, 96, 118),
        (97, 80, 134, 117), (135, 80, 167, 115), (170, 79, 202, 117),
        (206, 79, 232, 117), (238, 80, 262, 117), (263, 80, 293, 117),
        (295, 80, 331, 117), (334, 80, 366, 116), (370, 79, 399, 117),
    ),
    (
        (1, 124, 34, 164), (39, 124, 74, 163), (89, 125, 124, 163),
        (130, 121, 164, 163), (181, 122, 215, 163), (228, 122, 261, 162),
    ),
    (
        (1, 169, 30, 199), (35, 167, 64, 198), (67, 169, 97, 198),
        (98, 169, 129, 198), (131, 168, 160, 198), (162, 168, 191, 199),
        (193, 170, 223, 199), (230, 170, 261, 199), (268, 170, 298, 200),
    ),
    (
        (1, 206, 31, 233), (36, 206, 65, 233), (70, 206, 99, 233),
        (105, 206, 134, 233), (139, 206, 168, 233), (174, 206, 203, 233),
    ),
    (
        (1, 239, 30, 274), (36, 239, 66, 274), (74, 239, 105, 274),
        (111, 238, 142, 274), (149, 239, 179, 274), (186, 238, 217, 274),
    ),
    (
        (1, 283, 30, 318), (36, 283, 66, 318), (72, 286, 111, 317),
        (123, 285, 162, 317), (172, 286, 211, 317), (218, 285, 256, 317),
    ),
    (
        (1, 326, 25, 371), (31, 327, 60, 371), (65, 327, 85, 371),
        (90, 327, 115, 370), (119, 327, 144, 370), (149, 327, 169, 371),
        (184, 341, 224, 369), (232, 341, 271, 368),
    ),
    (
        (1, 379, 28, 417), (31, 379, 62, 415), (64, 379, 95, 415),
        (99, 377, 132, 415), (136, 379, 168, 415), (176, 377, 209, 416),
        (217, 379, 250, 416), (254, 378, 287, 414),
    ),
    (
        (6, 429, 40, 469), (49, 426, 83, 469),
        (96, 427, 119, 466), (125, 427, 148, 466),
    ),
)


def draw_frame(sprite_sheet, frame_box):
    left, top, right, bottom = frame_box
    frame_width = right - left
    frame_height = bottom - top
    source_y = sprite_sheet.h - bottom

    clear_canvas()
    sprite_sheet.clip_draw(
        left,
        source_y,
        frame_width,
        frame_height,
        CANVAS_WIDTH // 2,
        CANVAS_HEIGHT // 2,
        frame_width * FRAME_SCALE,
        frame_height * FRAME_SCALE,
    )
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
    return True


def play_animation(sprite_sheet, frame_boxes):
    for _ in range(ANIMATION_REPEAT_COUNT):
        for frame_box in frame_boxes:
            if not handle_events():
                return False
            draw_frame(sprite_sheet, frame_box)
            delay(FRAME_DELAY)
    return True


def wait_between_animations():
    delay(ANIMATION_PAUSE)
    return handle_events()


def play_all_animations(sprite_sheet):
    while True:
        for frame_boxes in ANIMATION_FRAME_BOXES:
            if not play_animation(sprite_sheet, frame_boxes):
                return False
            if not wait_between_animations():
                return False


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite_sheet = load_image(str(SPRITE_PATH))
        play_all_animations(sprite_sheet)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
