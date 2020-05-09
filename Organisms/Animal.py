from .Organism import Organism
import random


class Animal(Organism):

    def move(self):
        pomPositions = self.getNeighboringPositions()
        if pomPositions:
            newPosition = random.choice(pomPositions)
            metOrganism = self.world.getOrganismFromPosition(newPosition)
            self.world.say('{} moves from {} to {}'.format(self, self.position, newPosition))
            self.position = newPosition
            if metOrganism is not None:
                metOrganism.consequences(self)

    def action(self):
        birthPositions = self.getNeighboringBirthPositions()

        if self.ifReproduce() and birthPositions:
            newPosition = random.choice(birthPositions)
            newAnimal = self.__class__(newPosition, self.world)
            self.world.say('{} is born at {}'.format(newAnimal, newPosition))
            self.power = self.power / 2
            self.world.addOrganism(newAnimal)

    def getNeighboringPositions(self):
        return self.world.getNeighboringPositions(self.position)

    def getNeighboringBirthPositions(self):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))
