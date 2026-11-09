#reset world 일부분 지우고 게임월드 리스트 초기화
#world = [] #객체들의 리스트, 빈 리스트
world = [[], []] #리스트의 리스트? 


def clear():
    for layer in world:
        layer.clear()


def add_object(o, depth = 0):#기본값을 0으로 설정
    world[depth].append(o) #객체를 게임월드에 추가하는거

def remove_object(o):
    for layer in world: #모든 레이어를 순회하면서 객체를 제거
        if o in layer: #객체가 해당 레이어에 존재하면 제거
            layer.remove(o)
            return #객체 제거후 함수 종료

   


def update():
    # 업데이트 중 공이 제거되어도 다음 객체를 건너뛰지 않도록 복사본 순회
    for layer in world:
        for o in layer[:]: #[:] 이건 딱히 필요없는거라네
            o.update() #게임로직 때온거 여기다가 분리하네

#게임월드렌더링
def render():
    for layer in world:
        for o in layer:
            o.draw()
