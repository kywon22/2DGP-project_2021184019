import game_framework
import title_state
from pico2d import *
import mcharacter_state

running = True
image = None
people = 1

def enter():
    global image
    image = load_image('menu.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    pass

def draw():
    clear_canvas()
    mcharacter_state.draw_world()
    image.draw(700, 650)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
         match event.key:
             case pico2d.SDLK_ESCAPE:
                game_framework.pop_state()
             case pico2d.SDLK_1:
                people + 1
                play_state.boy.boy = 'plus'
                game_framework.pop_state()
             case pico2d.SDLK_2:
                people - 1
                if people > 1:
                    play_state.boy.boy = None
                    game_framework.pop_state()






