from .Organism import Organism
from Action import *
import random


class Animal(Organism):

    def move(self):
        result = []
        pomPositions = self.getNeighboringPositions()
        newPosition = None

        if pomPositions:
            newPosition = random.choice(pomPositions)
            result.append(Move(self, newPosition))
            metOrganism = self.world.getOrganismFromPosition(newPosition)
            if metOrganism is not None:
                result.extend(metOrganism.consequences(self))
        return result

    def action(self):
        result = []
        newAnimal = None
        birthPositions = self.getNeighboringBirthPositions()

        if self.ifReproduce() and birthPositions:
            newAnimalPosition = random.choice(birthPositions)
            newAnimal = self.clone()
            newAnimal.initParams()
            newAnimal.position = newAnimalPosition
            self.power = self.power / 2
            result.append(Add(newAnimal))
        return result

    def getNeighboringPositions(self):
        return self.world.getNeighboringPositions(self.position)

    def getNeighboringBirthPositions(self):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))
