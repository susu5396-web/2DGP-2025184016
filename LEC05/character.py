import math
from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

center_x, center_y = 400, 300
radius = 200

angle = 0
running = True

while running:
    clear_canvas()
    grass.draw(400, 30)
    
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    
    character.draw(x, y)
    update_canvas()
    
    angle += 0.05 
   
            
    delay(0.03)

close_canvas()
