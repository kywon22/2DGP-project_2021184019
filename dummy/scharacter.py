import game_framework
from pico2d import *
import game_world
from ball import Ball
import server


PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)
key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_w): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_s): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_a): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_w): UPKEY_UP,
    (SDL_KEYUP, SDLK_s): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class WalkingState:
    def enter(scharacter, event):
        if event == RIGHTKEY_DOWN:
            scharacter.x_velocity += RUN_SPEED_PPS
        elif event == RIGHTKEY_UP:
            scharacter.x_velocity -= RUN_SPEED_PPS
        if event == LEFTKEY_DOWN:
            scharacter.x_velocity -= RUN_SPEED_PPS
        elif event == LEFTKEY_UP:
            scharacter.x_velocity += RUN_SPEED_PPS

        if event == UPKEY_DOWN:
            scharacter.y_velocity += RUN_SPEED_PPS
        elif event == UPKEY_UP:
            scharacter.y_velocity -= RUN_SPEED_PPS
        if event == DOWNKEY_DOWN:
            scharacter.y_velocity -= RUN_SPEED_PPS
        elif event == DOWNKEY_UP:
            scharacter.y_velocity += RUN_SPEED_PPS

    def exit(scharacter, event):
        scharacter.face_x = scharacter.x_velocity
        if event == SPACE:
            scharacter.fire_ball()

    def do(scharacter):
        scharacter.frame = (scharacter.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        scharacter.x += scharacter.x_velocity * game_framework.frame_time
        scharacter.y += scharacter.y_velocity * game_framework.frame_time


    def draw(scharacter): #방향 좌표 확인해야함
        cx, cy = server.background.canvas_width // 2, server.background.canvas_height // 2
        scharacter.font.draw(cx - 40, cy + 40, '(%d, %d)' % (scharacter.x, scharacter.y), (255, 255, 0))
        if scharacter.x_velocity > 0:
            scharacter.image.clip_draw(int(scharacter.frame) * 30, 0, 30, 30, cx, cy)
            scharacter.dir = 1
        elif scharacter.x_velocity < 0:
            scharacter.image.clip_draw(int(scharacter.frame) * 30, 30, 30, 30, cx, cy)
            scharacter.dir = -1
        else:
            if scharacter.y_velocity > 0 or scharacter.y_velocity < 0:
                if scharacter.dir == 1:
                    scharacter.image.clip_draw(int(scharacter.frame) * 30, 60, 30, 30, cx, cy)
                else:
                    scharacter.image.clip_draw(int(scharacter.frame) * 30, 90, 30, 30, cx, cy)
            else:
                if scharacter.dir == -1:
                    scharacter.image.clip_draw(int(scharacter.frame) * 30, 90, 30, 30, cx, cy)
                else:
                    scharacter.image.clip_draw(int(scharacter.frame) * 30, 60, 30, 30, cx, cy)


next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}


class Scharacter:

    def __init__(self):
        self.image = load_image('main_character.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.x_velocity, self.y_velocity = 0, 0
        self.frame = 0
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.x, self.y = 500, 300


    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fire_ball(self):
        print('FIRE BALL')
        ball = Ball(self.x, self.y, self.face_x*2)
        game_world.add_object(ball, 1)
