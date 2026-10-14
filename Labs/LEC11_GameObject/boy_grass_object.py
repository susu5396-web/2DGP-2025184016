from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30) #이미지 중심을 화면에 400,30 에 놓아라
    def update(self):pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(1,1000)
        self.y = 90
        self.frame = random.randint(0, 7)
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        
class Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = 80
        self.y = 90

class Zombie:
    def __init__(self):
        self.x = 100
        self.y = 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5
    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y,
                             frame_width//2, frame_height//2)

def reset_world():
    global running
    running = True

    global world 
    world = []
    grass = Grass()
    world.append(grass)
    world.append(Zombie())

    team = [Boy() for i in range(11)]
    world += team

    

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()
reset_world() #초기 world 설정
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)



close_canvas()
