from dino_runner.components.power_ups.shield import Shield
import random
import pygame


class PowerUpManager():

    def __init__(self):
        self.power_ups = []
        self.points =  0
        self.when_appears = 0


    def update(self, game_speed, points, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                #power_up.start_time = pygame.time.get_ticks()
                player.shield_time_up = power_up.start_time + (random.randrange(5,7) * 1000)
                self.power_ups.remove(power_up)

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                self.when_appears = random.randint(self.when_appears + 50, self.when_appears + 100)
                self.power_ups.append(Shield())

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)