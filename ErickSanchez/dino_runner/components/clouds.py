import random
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_WIDTH
import pygame
from pygame.sprite import Sprite

class Cloud(Sprite):



    def __init__(self):

        self.image = CLOUD
        self.game_speed = 20
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.cloud_rect.y = random.randint(50, 100)
        
        self.width = self.image.get_width()

    def update(self):
        self.cloud_rect.x -= self.game_speed
        if self.cloud_rect.x < -self.width:
            self.cloud_rect.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.cloud_rect.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))