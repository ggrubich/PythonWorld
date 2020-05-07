from .Organism import Organism
from Action import *

import random

class Alien(Organism):

    def initParams(self):
        self.power = 10
        self.initiative = 20
        self.liveLength = 15
        self.powerToReproduce = 12
        self.sign = 'X'

    def move(self):
        result = []
        positions = self.world.filterFreePositions(
            self.world.getNeighboringPositions(self.position)
        )
        if len(positions) > 0:
            pos = random.choice(positions)
            result.append(Move(self, pos))
        return result

    def action(self):
        organisms = filter(
            lambda x: x is not None and not x.frozen,
            map(
                self.world.getOrganismFromPosition,
                self.world.getNeighboringPositions(self.position)
            )
        )
        result = list(map(Freeze, organisms))
        return result
