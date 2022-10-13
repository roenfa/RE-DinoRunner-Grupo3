import imp
from dino_runner.components import dinosaur
from dino_runner.components import game
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_HEIGHT

import random


class Cactus(Obstacle):

    def __init__(self, image,):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300
        