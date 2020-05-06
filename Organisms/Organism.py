from Action import *

from abc import ABC, abstractmethod

class Organism(ABC):

    def __init__(self, organism=None, position=None, world=None):
        self.power = None
        self.initiative = None
        self.position = None
        self.liveLength = None
        self.powerToReproduce = None
        self.sign = None
        self.world = None

        if organism is not None:
            self.power = organism.power
            self.initiative = organism.initiative
            self.position = organism.position
            self.liveLength = organism.liveLength
            self.powerToReproduce = organism.powerToReproduce
            self.sign = organism.sign
            self.world = organism.world
        else:
            if position is not None:
                self.position = position
            if world is not None:
                self.world = world
            self.initParams()


    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def initParams(self):
        pass

    @abstractmethod
    def clone(self):
        pass

    def consequences(self, atackingOrganism):
        result = []

        if self.power > atackingOrganism.power:
            result.append(Remove(atackingOrganism))
        else:
            result.append(Remove(self))
        return result

    def ifReproduce(self):
        result = False

        if self.power >= self.powerToReproduce:
            result = True
        return result

    def __str__(self):
        return '{0}: power: {1} initiative: {2} liveLength {3} position: {4}'\
                .format(self.__class__.__name__, self.power, self.initiative, self.liveLength, self.position)
