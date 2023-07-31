# This file is for strategy

from util.objects import *
from util.routines import *


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        speed = 900
        self.set_intent(drive(speed))
        print(f' my x position is: {self.me.location.x}')
        self.set_intent(atba())
        self.set_intent(goto(self.foe_goal.location))