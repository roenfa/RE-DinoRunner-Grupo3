import pygame

from dino_runner.components import text_utilis
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,RUNNING
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_hearth_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player=Dinosaur()
        self.obstacle_manager=ObstacleManager()

        self.points=0
        self.running=True
        self.death_count=0

        self.player_heart_manager=PlayerHeartManager()
        self.power_up_manager=PowerUpManager()
       
    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles(self)
        self.player_heart_manager.reduce_heart()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def execute(self):
        while self.running:
          if not self.playing:
            self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running=False
        self.screen.fill((255,255,255))

    def update(self):
        user_input=pygame.key.get_pressed()
        self.player.update()
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.game_speed, self.points, self.player)

    def draw(self):
        self.score()
        self.clock.tick(FPS)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        #tupla en xy
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points +=1
        if self.points % 100 ==0:
           self.game_speed +=1
        text, text_rect= text_utilis.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    def handle_key_event_on_menu(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
                self.playing=False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_heigh= SCREEN_HEIGHT // 2
        half_screen_widt=SCREEN_WIDTH // 2

        if self.death_count ==0:
            text, text_rect=text_utilis.get_centered_message('Press any key to Start')
            self.screen.blit(text, text_rect)
        elif self.death_count >0:
            text, text_rect=text_utilis.get_centered_message('Press any key to Restart')
            score, score_rect=text_utilis.get_centered_message('Your Score' + str(self.points), height=half_screen_heigh + 50)
            death, death_rect=text_utilis.get_centered_message('Death count'+ str(self.death_count), height=half_screen_heigh +100)
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, death_rect)
        self.screen.blit(RUNNING[0],(half_screen_widt -20, half_screen_heigh -140))
    
    def show_menu(self):
        self.running=True

        while_color= (255,255,255)
        self.screen.fill(while_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_event_on_menu()
            