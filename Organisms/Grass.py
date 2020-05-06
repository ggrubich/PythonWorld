from .Plant import Plant


class Grass(Plant):

    def initParams(self):
        self.power = 0
        self.initiative = 0
        self.liveLength = 6
        self.powerToReproduce = 3
        self.sign = 'G'
