#reset world 일부분 지우고 게임월드 리스트 초기화
world = [] #객체들의 리스트, 빈 리스트

def add_object(o):
    world.append(o) #객체를 게임월드에 추가하는거

def remove_object(o):
    world.remove(o)


def update():
    # 업데이트 중 공이 제거되어도 다음 객체를 건너뛰지 않도록 복사본 순회
    for o in world[:]:
        o.update() #게임로직 때온거 여기다가 분리하네

#게임월드렌더링
def render():
    for o in world:
        o.draw()
