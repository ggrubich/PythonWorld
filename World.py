from Position import Position
from Organisms.Plant import Plant


class World(object):

    def __init__(self, worldX, worldY):
        self._worldX = worldX
        self._worldY = worldY
        self._turn = 0
        self._organisms = []
        self._newOrganisms = []
        self._separator = ' '

    def makeTurn(self):
        actions = []

        queue = self._organisms.copy()
        queue.sort(key=lambda o: o.initiative, reverse=True)
        for org in queue:
            if not org.frozen and self.positionOnBoard(org.position):
                actions = org.move()
                for a in actions:
                    self.makeMove(a)
                actions = []
                if self.positionOnBoard(org.position):
                    actions = org.action()
                    for a in actions:
                        self.makeMove(a)
                    actions = []

        for org in self._organisms:
            if not org.frozen:
                org.liveLength -= 1
                org.power += 1
            org.frozen = False
            if org.liveLength < 1:
                print(str(org.__class__.__name__) + ': died of old age at: ' + str(org.position))
        self._organisms = [o for o in self._organisms if o.liveLength > 0]

        self._organisms.extend(self._newOrganisms)
        self._newOrganisms = []

        self._turn += 1

    def makeMove(self, action):
        print(action)
        action.run()

    def addOrganism(self, newOrganism):
        self._organisms.append(newOrganism)

    def scheduleOrganism(self, organism):
        self._newOrganisms.append(organism)

    def removeOrganism(self, organism):
        self._organisms.remove(organism)
        organism.position = Position.invalid()

    def positionOnBoard(self, position):
        return position.x >= 0 and position.y >= 0 and position.x < self._worldX and position.y < self._worldY

    def getOrganismFromPosition(self, position):
        for org in self._organisms:
            if org.position == position:
                return org
        return None

    def getNeighboringPositions(self, position):
        result = []
        pomPosition = None

        for y in range(-1, 2):
            for x in range(-1, 2):
                pomPosition = Position(position.x + x, position.y + y)
                if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
                    result.append(pomPosition)
        return result

    def filterFreePositions(self, fields):
        result = []

        for field in fields:
            if self.getOrganismFromPosition(field) is None:
                result.append(field)
        return result

    def filterPositionsWithoutAnimals(self, fields):
        result = []
        pomOrg = None

        for filed in fields:
            pomOrg = self.getOrganismFromPosition(filed)
            if pomOrg is None or isinstance(pomOrg, Plant):
                result.append(filed)
        return result

    def filterPositionsWithOtherSpecies(self, fields, species):
        result = []
        for filed in fields:
            pomOrg = self.getOrganismFromPosition(filed)
            if not isinstance(pomOrg, species):
                result.append(filed)
        return result

    def __str__(self):
        result = '\nturn: ' + str(self._turn) + '\n'
        for wY in range(0, self._worldY):
            for wX in range(0, self._worldX):
                org = self.getOrganismFromPosition(Position(wX, wY))
                if org:
                    result += str(org.sign)
                else:
                    result += self._separator
            result += '\n'
        return result
