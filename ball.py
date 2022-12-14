from pico2d import *
import game_world
import random

class Ball:
    image = None

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('waterball.png')
        self.x, self.y, self.velocity = random.randint(0, 400),  random.randint(600, 15000), 10

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.y -= 1

        if self.y < 0:
            game_world.remove_object(self)

