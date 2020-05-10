from .Organism import Organism
import random


class Animal(Organism):

    def __init__(self, position, world):
        super().__init__(position, world)
        self.stomach = []

    def freeze(self):
        for _, org in self.stomach:
            org.freeze()
        super().freeze()

    def unfreeze(self):
        for _, org in self.stomach:
            org.unfreeze()
        super().unfreeze()

    def add(self):
        for org in self.stomach:
            org.add()
        super().add()

    def remove(self):
        for org in self.stomach:
            org.remove()
        super().remove()

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
        self.spitOut()

        birthPositions = self.getNeighboringBirthPositions()

        if self.ifReproduce() and birthPositions:
            newPosition = random.choice(birthPositions)
            newAnimal = self.__class__(newPosition, self.world)
            self.world.say('{} is born at {}'.format(newAnimal, newPosition))
            self.power = self.power / 2
            newAnimal.add()

    def swallow(self, organism):
        self.stomach.append((self.world.turn, organism))

    def spitOut(self):
        out = []
        leave = []
        for turn, org in self.stomach:
            if turn < self.world.turn:
                out.append((turn, org))
            else:
                leave.append((turn, org))
        while len(out) > 0:
            positions = self.world.filterFreePositions(
                self.world.getNeighboringPositions(self.position)
            )
            if len(positions) == 0:
                break
            destPos = random.choice(positions)
            _, org = out.pop()
            self.world.say('{} spits out {} to {}'.format(self, org, destPos))
            org.position = destPos
        self.stomach = out + leave

    def getNeighboringPositions(self):
        return self.world.getNeighboringPositions(self.position)

    def getNeighboringBirthPositions(self):
        return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))
