from sre_constants import JUMP
from dino_runner.utils.constants import (RUNNING, RUNNING_SHIELD, DUCKING, DUCKING_SHIELD)
from pygame.sprite import Sprite
import pygame

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 15
    JUMP_HEIGHT= 150

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.back = False

        self.dino_run = True
        self.dino_duck = False
        self.dino_duck_counter = 0
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.shield = False
        self.shield_time_up = 0
        self.timer_event = pygame.USEREVENT + 1

    def update(self):
        if self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        else:
            self.run()
        if self.step_index >= 10:
            self.step_index = 0
        if self.dino_duck_counter >= 20:
            self.dino_duck = False
            self.dino_duck_counter = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def event(self):
        pass

    def run(self):
        if self.shield:
            self.image = RUNNING_SHIELD[0] if self.step_index < 5 else RUNNING_SHIELD[1]
        else:
            self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]                  

        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS 
        self.step_index +=1

    def jump(self):

        if self.shield:
            self.image = RUNNING_SHIELD[0]
        else:
            self.image = RUNNING[0]               
        self.dino_rect.x = self.X_POS
        
        if self.dino_rect.y <= self.JUMP_HEIGHT and not self.back:
            self.back = True
        elif not self.back and self.dino_rect.y > self.JUMP_HEIGHT:
            self.dino_rect.y -= self.jump_vel
        elif self.back and self.dino_rect.y < self.Y_POS:
            self.dino_rect.y += self.jump_vel
        elif self.back and self.dino_rect.y >= self.Y_POS:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.back = False
        self.step_index +=1

    def duck(self):
        if self.shield:
            self.image = DUCKING_SHIELD[0] if self.step_index < 5 else DUCKING_SHIELD[1]
        else:
            self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS 
        self.dino_rect.y = self.Y_POS + self.dino_rect.height/2
        self.step_index +=1
        self.dino_duck_counter +=1

