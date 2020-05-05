from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Position(object):

    x: int
    y: int

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    @staticmethod
    def invalid():
        return Position(-1, -1)

    def isInvalid(self):
        return self.x < 0 or self.y < 0
