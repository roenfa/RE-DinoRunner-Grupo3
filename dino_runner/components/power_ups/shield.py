from random import randint
from shelve import Shelf
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUp):
    
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        self.speed = randint(5,10)
        super().__init__(self.image, self.type, self.speed)
