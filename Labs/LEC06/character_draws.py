from pico2d import*

open_canvas(800,600)
character = load_image('character.png')


def move_circle():
    for degree in range(0,360,5):
        theta = math.radians(degree)
        x = 400 + 200*math.cos(theta)
        y = 300 + 200*math.sin(theta)
        draw_character(x,y)
    pass
def move_top():
    for x in range(50,750,5):
        draw_character(x,550)

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.05)

def move_right():
    for y in range(550,50,-5):
        draw_character(750,y)

def move_bottom():
    print("BOTTOM")
    pass
def move_left():
    print("LEFT")
    pass

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
   
    pass
def move_triangle():
    print("Triangle")
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()