from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.utils.constants import (
    SMALL_CACTUS, LARGE_CACTUS, BIRD
)
from dino_runner.components.dinosaur import Dinosaur
import random
import  pygame


class ObstacleManager:

    def __init__(self):
        self.obstacles = []


    def update(self, game):
        #if len(self.obstacles) == 0:
        #    cactus_size = random.randint(0,2)
        #    if cactus_size == 0:
        #        self.obstacles.append(LargeCactus(LARGE_CACTUS))
        #    elif cactus_size ==1:
        #        self.obstacles.append(SmallCactus(SMALL_CACTUS))
             
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

                    
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(100)
                self.obstacles = []

                game.player_heart_manager.reduce_heart()
                if game.player_heart_manager.heart_count > 0:
                    game.player.show_text = False

                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self1):
        self.obstacles = []
        