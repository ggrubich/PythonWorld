from .Plant import Plant


class Dandelion(Plant):

    def clone(self):
        return Dandelion(self, None, None)

    def initParams(self):
        self.power = 0
        self.initiative = 0
        self.liveLength = 6
        self.powerToReproduce = 2
        self.sign = 'D'
