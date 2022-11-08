import random
import json
import os

from pico2d import *
import game_framework
import game_world

from mcharacter import Mcharacter
# from background import TileBackground as Background
# from background import FixedBackground as Background
from background import InfiniteBackground as Background


import server


name = "MainState"



def enter():
    server.mcharacter = Mcharacter()
    game_world.add_object(server.mcharacter, 1)

    server.background = Background()
    game_world.add_object(server.background, 0)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.mcharacter.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






