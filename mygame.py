import pico2d
import game_framework
import mcharacter_state
import logo_state
#import item_state

pico2d.open_canvas()
game_framework.run(mcharacter_state)
pico2d.close_canvas()
