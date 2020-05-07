from Action import *

from abc import ABC, abstractmethod


class Organism(ABC):

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

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def action(self):
        pass

    def consequences(self, attackingOrganism):
        result = []
        if self.frozen or attackingOrganism.power >= self.power:
            result.append(Remove(self))
        else:
            result.append(Remove(attackingOrganism))
        return result

    def ifReproduce(self):
        return self.power >= self.powerToReproduce

    def __str__(self):
        return '{0}: power: {1} initiative: {2} liveLength {3} position: {4}'\
                .format(self.__class__.__name__, self.power, self.initiative, self.liveLength, self.position)
