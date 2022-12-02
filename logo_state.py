import game_framework
import title_state
from pico2d import *

running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('logo.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    # global running
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    clear_canvas()
    image.draw(197, 400)
    update_canvas()
    pass

def handle_events():
    events = get_events()





