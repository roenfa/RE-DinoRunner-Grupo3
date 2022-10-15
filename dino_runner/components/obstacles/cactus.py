from dino_runner.components.obstacles.obstacle import Obstacle
import random
import pygame
from pygame.sprite import Sprite


class Cactus(Obstacle):
    

    def __init__(self, image, description):
        self.image = image
        self.type = random.randint(0, 2)
        rect = self.image[self.type].get_rect()
        self.description = description
        super().__init__(self.image, self.type, self.description)
        self.rect.y = 400 - rect.height
        