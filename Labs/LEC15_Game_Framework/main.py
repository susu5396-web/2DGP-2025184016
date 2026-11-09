from pico2d import *
from Labs.LEC12_CharacterController.main import render_world
import play_mode


open_canvas()
play_mode.init()
# game loop
while play_mode.running:
    play_mode.handle_events()
    play_mode.update()
    play_mode.render()
    delay(0.01)
# finalization code
play_mode.finish()
close_canvas()
