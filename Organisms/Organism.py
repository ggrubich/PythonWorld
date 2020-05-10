from abc import ABC, abstractmethod


class Organism(ABC):

    def __init_subclass__(cls):
        if 'name' not in cls.__dict__:
            cls.name = cls.__name__
        super().__init_subclass__()

    def __init__(self, position, world):
        # state
        self.position = position
        self.world = world
        self.frozen = False

        # params
        self.power = None
        self.initiative = None
        self.liveLength = None
        self.powerToReproduce = None
        self.sign = None
        self.initParams()

    @abstractmethod
    def initParams(self):
        pass

    def freeze(self):
        self.frozen = True

    def unfreeze(self):
        self.frozen = False

    def add(self):
        self.world.addOrganism(self)

    def remove(self):
        self.world.removeOrganism(self)

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def action(self):
        pass

    def consequences(self, attacker):
        if self.frozen or attacker.power >= self.power:
            winner, loser = attacker, self
        else:
            winner, loser = self, attacker
        self.world.say('{} gets eaten by {}'.format(loser, winner))
        loser.remove()

    def ifReproduce(self):
        return self.power >= self.powerToReproduce

    def __str__(self):
        return self.name
