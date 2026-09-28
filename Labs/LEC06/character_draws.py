from pico2d import*

open_canvas(800,600)
character = load_image('character.png')


def move_circle():
    for degree in range(0,360,4):
        theta = math.radians(degree)
        x = 400 + 200*math.cos(theta)
        y = 300 + 200*math.sin(theta)
        draw_character(x,y)
    
def move_top():
    for x in range(200,600,10):
        draw_character(x,450)

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.03)

def move_right():
    for y in range(450,150,-10):
        draw_character(600,y)

def move_bottom():
    for x in range(600,200,-10):
        draw_character(x,150)
    
def move_left():
    for y in range(150,450,10):
        draw_character(200,y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
   
    
def move_triangle_up():
    x = 100
    y = 100

    for z in range(51):
       draw_character(x, y)
       x += 6
       y += 8


def move_triangle_down():
    x = 400
    y = 500

    for z in range(51):
        draw_character(x,y)
        x += 6
        y -= 8

def move_triangle_bottom():
    x = 700
    y = 100

    for z in range(51):
        draw_character(x,y)
        x -= 12

 

def move_triangle():
    move_triangle_up()
    move_triangle_down()
    move_triangle_bottom()


while True:
    move_circle()
    move_rectangle()
    move_triangle()


close_canvas()