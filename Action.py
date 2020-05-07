from __future__ import annotations

from Organisms.Organism import *
from Position import Position

from abc import ABC, abstractmethod
from dataclasses import dataclass


__all__ = [
    'Action',
    'Add',
    'Remove',
    'Move',
    'Freeze',
]

class Action(ABC):

    @abstractmethod
    def run(self):
        pass

def name(organism):
    return organism.__class__.__name__

@dataclass
class Add(Action):

    organism: Organism

    def __str__(self):
        return '{}: add at {}'.format(name(self.organism), self.organism.position)

    def run(self):
        world = self.organism.world
        world.scheduleOrganism(self.organism)

@dataclass
class Remove(Action):

    organism: Organism

    def __str__(self):
        return '{}: remove from {}'.format(name(self.organism), self.organism.position)

    def run(self):
        world = self.organism.world
        world.removeOrganism(self.organism)

@dataclass
class Move(Action):

    organism: Organism
    position: Position

    def __str__(self):
        return '{}: move from {} to {}'.format(name(self.organism), self.organism.position, self.position)

    def run(self):
        self.organism.position = self.position

@dataclass
class Freeze(Action):

    organism: Organism

    def __str__(self):
        return '{}: gets frozen'.format(name(self.organism))

    def run(self):
        self.organism.frozen = True
