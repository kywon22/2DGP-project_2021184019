from pico2d import *

stage_WIDTH, stage_HEIGHT = 700, 650

def handle_events():
    global running
    global dir1, dir2
    global direct

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir1 += 1
                direct = 0
            elif event.key == SDLK_LEFT:
                dir1 -= 1
                direct = 1
            if event.key == SDLK_UP:
                dir2 += 1
                direct = 2
            elif event.key == SDLK_DOWN:
                dir2 -= 1
                direct = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir1 -= 1
            elif event.key == SDLK_LEFT:
                dir1 += 1
            if event.key == SDLK_UP:
                dir2 -= 1
            elif event.key == SDLK_DOWN:
                dir2 += 1
    pass

open_canvas()
stage_ground = load_image('stay stage.png')
character = load_image('stage1-1 monster1.png')

running = True
x = 700 // 2
y = 650 // 2
direct = 2
frame = 0
dir1, dir2 = 0, 0

while running:
    clear_canvas()
    stage_ground.draw(stage_WIDTH // 2, stage_HEIGHT // 2)
    character.clip_draw(frame * 30, 30 * direct, 20, 20, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    x += dir1 * 5
    y += dir2 * 5
    delay(0.04)

close_canvas()
