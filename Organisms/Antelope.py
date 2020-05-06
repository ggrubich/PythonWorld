from .Animal import Animal
from .Wolf import Wolf
from Position import Position
from Action import *


class Antelope(Animal):

    def initParams(self):
        self.power = 3
        self.initiative = 10
        self.liveLength = 10
        self.powerToReproduce = 6
        self.sign = "A"

    def move(self):
        for pos in self.world.getNeighboringPositions(self.position):
            neighbor = self.world.getOrganismFromPosition(pos)
            if isinstance(neighbor, Wolf):
                return self.escape(neighbor)
        return super().move()

    def escape(self, threat):
        pos = Position(
            self.position.x + 2 * (self.position.x - threat.position.x),
            self.position.y + 2 * (self.position.y - threat.position.y),
        )
        destPos = pos if self.world.positionOnBoard(pos) else threat.position
        destOrg = self.world.getOrganismFromPosition(destPos)
        result = [Move(self, destPos)]
        if destOrg is not None:
            result.extend(destOrg.consequences(self))
        return result

    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(
            self.world.getNeighboringPositions(self.position)
        )
