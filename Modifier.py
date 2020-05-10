from abc import ABC, abstractmethod
from collections import Counter
from itertools import groupby
import statistics


__all__ = [
    'Modifier',
    'KillExcessive',
]

class Modifier(ABC):

    @abstractmethod
    def apply(self, world):
        pass

class KillExcessive(Modifier):

    def __init__(self, triggerRatio, resultRatio):
        self.triggerRatio = triggerRatio
        self.resultRatio = resultRatio

    def getExcessive(self, world):
        groupedOrgs = [list(g) for k, g in
            groupby(world.allOrganisms(), lambda org: org.__class__)
        ]
        mean = statistics.mean(len(orgs) for orgs in groupedOrgs)
        excessive = []
        for orgs in groupedOrgs:
            if len(orgs) > self.triggerRatio * mean:
                orgs.sort(key=lambda org: org.liveLength)
                while len(orgs) > self.resultRatio * mean:
                    excessive.append(orgs.pop())
        return excessive

    def apply(self, world):
        excessive = self.getExcessive(world)
        for org in excessive:
            world.say('excessive {} removed from {}'.format(org, org.position))
            org.remove()
