from .Animal import Animal
from Position import Position


class Turtle(Animal):

    def initParams(self):
        self.power = 3
        self.initiative = 3
        self.liveLength = 30
        self.powerToReproduce = 18
        self.sign = 'T'

    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

    def consequences(self, attacker):
        if isinstance(attacker, Animal) and attacker.power >= self.power:
            self.world.say('{} eats {} at {}'.format(attacker, self, attacker.position))
            self.position = Position.invalid()
            attacker.swallow(self)
        else:
            super().consequences(attacker)
