from random import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import (
    SMALL_CACTUS, LARGE_CACTUS
)
from dino_runner.components.dinosaur import Dinosaur
import random
import pygame


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0,1)
            if cactus_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(5000)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

