from .Organism import Organism
from Action import *
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
                newPlant = self.clone()
                newPlant.initParams()
                newPlant.position = newPosition
                self.power = self.power / 2
                result.append(Add(newPlant))
        return result

    def getFreeNeighboringPosition(self, position):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(position))
