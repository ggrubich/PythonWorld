from .Plant import Plant


class Toadstool(Plant):

    def initParams(self):
        self.power = 0
        self.initiative = 0
        self.liveLength = 10
        self.powerToReproduce = 5
        self.sign = 'T'

    def consequences(self, attacker):
        if self.power > attacker.power:
            self.world.say('{} gets poisoned by {}'.format(attacker, self))
            self.world.removeOrganism(attacker)
        else:
            self.world.say('{} eats {} and dies'.format(attacker, self))
            self.world.removeOrganism(attacker)
            self.world.removeOrganism(self)
