from dino_runner.utils.constants import (SCREEN_WIDTH, BIRD)
from pygame.sprite import Sprite

class Obstacle (Sprite):

    def __init__(self, image, type, description):
        self.image =image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.fly_index = 0
        self.description = description
        

    def update(self,game_speed, obstacles):
        self.rect.x -= game_speed
        if self.description == "bird":
            self.type = 0 if self.fly_index < 5 else 1
            # self.rect = self.image[self.type].get_rect()
            self.fly_index +=1
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
        if self.fly_index >= 10:
            self.fly_index = 0
        

    def draw(self, screen):
        screen.blit(self.image[self.type],self.rect)