from pico2d import *
import random

stage_WIDTH, stage_HEIGHT = 700, 650

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

open_canvas(stage_WIDTH, stage_HEIGHT)
stage_ground = load_image('stay stage.png')
character = load_image('stage1-1 monster1.png')

running = True
x = 700 // 2
y = 650 // 2
direct = 2
frame = 0
dir1, dir2 = 0, 0

running = True
sx, sy = stage_WIDTH // 2, stage_HEIGHT // 2
x, y = sx, sy
ax, ay = x, y
ro = 0
frame = 0
hide_cursor()

t = 0
def reset_world():
    global ax, ay
    global t
    global sx, sy

    ax, ay = random.randint(0, stage_WIDTH), random.randint(0, stage_HEIGHT)
    t = 0
    sx, sy = x, y
    pass

def update_world():
    global x, y
    global t
    global ro
    t += 0.005
    x = (1 - t) * sx + t * ax
    y = (1 - t) * sy + t * ay
    if ax>sx:
        ro=1
    if ax<sx:
        ro=0
    if t >= 1.0:
        reset_world()
    pass

reset_world()

while running:
    update_world()
    clear_canvas()
    stage_ground.draw(stage_WIDTH // 2, stage_HEIGHT // 2)
    character.clip_draw(frame * 30, 30 * direct, 20, 20, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3

close_canvas()
