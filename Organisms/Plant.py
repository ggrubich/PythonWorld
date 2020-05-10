from .Organism import Organism
import random


class Plant(Organism):

    def move(self):
        result = []
        return result

    def action(self):
        result = []
        newPlant = None
        newPosition = None

        if self.ifReproduce():
            pomPositions = self.getFreeNeighboringPosition(self.position)

            if pomPositions:
                newPosition = random.choice(pomPositions)
                newPlant = self.__class__(newPosition, self.world)
                self.world.say('{} spreads to {}'.format(newPlant, newPosition))
                self.power = self.power / 2
                newPlant.add()
        return result

    def getFreeNeighboringPosition(self, position):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(position))
