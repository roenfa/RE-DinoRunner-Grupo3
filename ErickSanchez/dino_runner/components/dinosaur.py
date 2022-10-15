from dino_runner.utils.constants import RUNNING
from dino_runner.utils.constants import JUMPING
from dino_runner.utils.constants import DUCKING
from pygame.sprite import Sprite
import pygame



class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.image_run = RUNNING[0]
        self.image_jump = JUMPING
        self.image_duck = DUCKING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.shield = False
        self.shiel_time_up = 0
        
        self.userInput = pygame.key
        
        self.step_index = 0
        self.image = RUNNING[0]
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False


        if self.step_index >=10:
            self.step_index = 0

       


    def event(self):
        pass
    
    
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1
    
    
    
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1



    def jump(self):
    
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL    

        
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

