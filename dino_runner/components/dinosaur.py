from sre_constants import JUMP
from dino_runner.utils.constants import RUNNING
from pygame.sprite import Sprite
import pygame

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0

        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.shield = False
        self.shield_time_up = 0

    def update(self):
        self.run()
        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def event(self):
        pass

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        # if self.step_index < 5:
        #     self.image = RUNNING[0]
        # else:
        #     self.image = RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index +=1