from .Animal import Animal


class Sheep(Animal):

    def clone(self):
        return Sheep(self, None, None)

    def initParams(self):
        self.power = 3
        self.initiative = 3
        self.liveLength = 10
        self.powerToReproduce = 6
        self.sign = 'S'

    def getNeighboringPositions(self):
        return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))
