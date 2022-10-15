from dino_runner.components.power_ups.power_up import Power_Up
from dino_runner.utils.constants import (
SHIELD, SHIELD_TYPE
)

class Shield(Power_Up):

    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(Shield,self).__init__(image = self.image, type = self.type)
