from .Plant import Plant


class Grass(Plant):

    def clone(self):
        return Grass(self, None, None)

    def initParams(self):
        self.power = 0
        self.initiative = 0
        self.liveLength = 6
        self.powerToReproduce = 3
        self.sign = 'G'
