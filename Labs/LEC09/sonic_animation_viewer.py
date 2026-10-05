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
)


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite_sheet = load_image(str(SPRITE_PATH))
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
