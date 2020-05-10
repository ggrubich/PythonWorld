from .Plant import Plant


class Dandelion(Plant):

    def initParams(self):
        self.power = 0
        self.initiative = 0
        self.liveLength = 6
        self.powerToReproduce = 2
        self.sign = 'd'
