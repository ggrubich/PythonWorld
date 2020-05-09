from .Animal import Animal
from .Wolf import Wolf
from Position import Position


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
        destPos = Position(
            self.position.x + 2 * (self.position.x - threat.position.x),
            self.position.y + 2 * (self.position.y - threat.position.y),
        )
        if self.world.positionOnBoard(destPos):
            self.world.say('{} escapes from {} from {} to {}'.format(
                self, threat, self.position, destPos
            ))
        else:
            self.world.say('{} desperately attacks {} at {}'.format(
                self, threat, threat.position
            ))
            destPos = threat.position
        destOrg = self.world.getOrganismFromPosition(destPos)
        self.position = destPos
        if destOrg is not None:
            destOrg.consequences(self)

    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(
            self.world.getNeighboringPositions(self.position)
        )
