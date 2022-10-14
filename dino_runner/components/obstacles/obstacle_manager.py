
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import (
    SMALL_CACTUS,LARGE_CACTUS
)

import random
import pygame


class ObstacleManager:

    def __init__(Self):
        Self.obstacles = []

    def update(self, game):
        
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0, 1) 
            if cactus_size == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            



