from pico2d import *

class Bottom1:
    def __init__(self):
        self.image = load_image('bottom.png')

    def draw(self):
        self.image.draw(100, 10)

    def update(self):
        pass

class Bottom2:
    def __init__(self):
        self.image = load_image('bottom.png')

    def draw(self):
        self.image.draw(350, 10)

    def update(self):
        pass

class Background:
    def __init__(self):
        self.image = load_image('stage.png')

    def draw(self):
        self.image.draw(240, 400)

    def update(self):
        pass

class Life1:
    def __init__(self):
        self.image = load_image('item.png')

    def draw(self):
        self.image.draw(300, 570)

    def update(self):
        pass

class Life2:
    def __init__(self):
        self.image = load_image('item.png')

    def draw(self):
        self.image.draw(335, 570)

    def update(self):
        pass

class Life3:
    def __init__(self):
        self.image = load_image('item.png')

    def draw(self):
        self.image.draw(370, 570)

    def update(self):
        pass