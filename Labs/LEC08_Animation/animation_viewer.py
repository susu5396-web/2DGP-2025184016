from pico2d import *

open_canvas(800, 800)

character = load_image('loopy_sprite_sheet.png')

clear_canvas()
character.draw(400, 400, 700, 700)
update_canvas()

delay(3)
close_canvas()