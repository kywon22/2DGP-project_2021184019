from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 800, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('waterball.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x += self.velocity
        if self.x < -1000 or self.x > 1000:
            game_world.remove_object(self)

