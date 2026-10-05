from pathlib import Path

from pico2d import close_canvas, load_image, open_canvas

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SPRITE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
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
)


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite_sheet = load_image(str(SPRITE_PATH))
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
