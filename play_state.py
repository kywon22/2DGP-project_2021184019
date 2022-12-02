from pico2d import *
import game_framework
import game_world
import gameover_state

from background import Bottom1
from background import Bottom2
from background import Life1
from background import Life2
from background import Life3
from background import Background
from maincharacter import Maincharacter
from ball import Ball



maincharacter = None
bottom1 = None
bottom2 = None
life1 = None
life2 = None
life3 = None
background = None
balls = []

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            maincharacter.handle_event(event)


# 초기화
def enter():
    global maincharacter, bottom1, bottom2, life1, life2, life3, background
    maincharacter = Maincharacter()
    bottom1 = Bottom1()
    bottom2 = Bottom2()
    life1 = Life1()
    life2 = Life2()
    life3 = Life3()
    background = Background()
    game_world.add_object(maincharacter, 3)
    game_world.add_object(bottom1, 2)
    game_world.add_object(bottom2, 2)
    game_world.add_object(life1, 2)
    game_world.add_object(life2, 2)
    game_world.add_object(life3, 2)
    game_world.add_object(background, 0)
    global balls
    balls = [Ball() for i in range(1000)]
    game_world.add_objects(balls, 1)

# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for ball in balls.copy():
        if collide(maincharacter, ball):
            game_framework.change_state(gameover_state)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True