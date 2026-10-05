from pico2d import close_canvas, open_canvas

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    close_canvas()


if __name__ == "__main__":
    main()
