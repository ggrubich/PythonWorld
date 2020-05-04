from .Animal import Animal
from .Wolf import Wolf
from Position import Position
from Action import Action
from ActionEnum import ActionEnum


class Antelope(Animal):
    def __init__(self, sheep=None, position=None, world=None):
        super().__init__(sheep, position, world)

    def clone(self):
        return Antelope(self, None, None)

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
            xPosition=self.position.x + 2 * (self.position.x - threat.position.x),
            yPosition=self.position.y + 2 * (self.position.y - threat.position.y),
        )
        destPos = pos if self.world.positionOnBoard(pos) else threat.position
        destOrg = self.world.getOrganismFromPosition(destPos)
        result = [Action(ActionEnum.A_MOVE, destPos, None, self)]
        if destOrg is not None:
            result.extend(destOrg.consequences(self))
        return result

    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(
            self.world.getNeighboringPositions(self.position)
        )
