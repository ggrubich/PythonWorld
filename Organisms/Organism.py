from Action import *

from abc import ABC, abstractmethod


class Organism(ABC):

    def __init__(self, position, world):
        self.position = position
        self.world = world
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

    def consequences(self, atackingOrganism):
        result = []

        if self.power > atackingOrganism.power:
            result.append(Remove(atackingOrganism))
        else:
            result.append(Remove(self))
        return result

    def ifReproduce(self):
        return self.power >= self.powerToReproduce

    def __str__(self):
        return '{0}: power: {1} initiative: {2} liveLength {3} position: {4}'\
                .format(self.__class__.__name__, self.power, self.initiative, self.liveLength, self.position)
