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
    for x in range(50,750,10):
        draw_character(x,550)

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.03)

def move_right():
    for y in range(550,50,-10):
        draw_character(750,y)

def move_bottom():
    for x in range(750,50,-10):
        draw_character(x,50)
    
def move_left():
    for y in range(50,550,10):
        draw_character(50,y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
   
    pass

def move_triangle_up():
    x = 100
    y = 100

    for z in range(51):
       draw_character(x, y)
       x += 3
       y += 4


def move_triangle_down():
    x = 400
    y = 500

    for z in range(51):
        draw_character(x,y)
        x += 3
        y -= 4

def move_triangle_bottom():
    x = 700
    y = 100

    for z in range(51):
        draw_character(x,y)
        x -= 6

    pass

def move_triangle():
    move_triangle_up()
    move_triangle_down()
    move_triangle_bottom()
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()