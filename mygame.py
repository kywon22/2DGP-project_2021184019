import game_framework
import pico2d
import logo_state

pico2d.open_canvas(400, 600)
game_framework.run(logo_state)
pico2d.close_canvas()