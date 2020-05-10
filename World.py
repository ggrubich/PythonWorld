from Position import Position
from Organisms.Plant import Plant


class World(object):

    def __init__(self, width, height, modifiers):
        self._width = width
        self._height = height
        self._turn = 0
        self._organisms = []
        self._separator = ' '
        self._log = []
        self._modifiers = modifiers

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def turn(self):
        return self._turn

    @property
    def log(self):
        return self._log

    def say(self, msg):
        self._log.append(msg)

    def makeTurn(self):
        self._log = []
        queue = self._organisms.copy()
        queue.sort(key=lambda o: o.initiative, reverse=True)
        for org in queue:
            if not org.frozen:
                if self.positionOnBoard(org.position):
                    org.move()
                if self.positionOnBoard(org.position):
                    org.action()

        for org in self._organisms:
            if not org.frozen:
                org.liveLength -= 1
                org.power += 1
            else:
                org.unfreeze()
            if org.liveLength < 1:
                self.say('{} died of old age at {}'.format(org, org.position))
        self._organisms = [o for o in self._organisms if o.liveLength > 0]
        for mod in self._modifiers:
            mod.apply(self)

        self._turn += 1

    def addOrganism(self, newOrganism):
        self._organisms.append(newOrganism)

    def removeOrganism(self, organism):
        self._organisms.remove(organism)
        organism.position = Position.invalid()

    def allOrganisms(self):
        return self._organisms

    def positionOnBoard(self, position):
        return position.x >= 0 and position.y >= 0 and position.x < self._width and position.y < self._height

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
        result += '┌'
        for x in range(self._height):
            result += '─'
        result += '┐\n'
        for y in range(0, self._height):
            result += '│'
            for x in range(0, self._width):
                org = self.getOrganismFromPosition(Position(x, y))
                if org:
                    result += str(org.sign)
                else:
                    result += self._separator
            result += '│\n'
        result += '└'
        for x in range(self._height):
            result += '─'
        result += '┘\n'
        return result
