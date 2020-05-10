from .Organism import Organism

import random

class Alien(Organism):

    def initParams(self):
        self.power = 10
        self.initiative = 20
        self.liveLength = 15
        self.powerToReproduce = 12
        self.sign = 'X'

    def move(self):
        positions = self.world.filterFreePositions(
            self.world.getNeighboringPositions(self.position)
        )
        if len(positions) > 0:
            pos = random.choice(positions)
            self.world.say('{} moves from {} to {}'.format(self, self.position, pos))
            self.position = pos

    def action(self):
        organisms = filter(
            lambda x: x is not None and not x.frozen,
            map(
                self.world.getOrganismFromPosition,
                self.world.getNeighboringPositions(self.position)
            )
        )
        for org in organisms:
            if not org.frozen:
                self.world.say('{} gets frozen by {} at {}'.format(org, self, org.position))
                org.freeze()
