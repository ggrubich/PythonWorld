from World import World
from Position import Position

import os


class Game(object):

    def __init__(self, width, height, knownOrganisms, startingOrganisms):
        self._knownOrganisms = knownOrganisms
        self._world = World(width, height)
        for cls, pos in startingOrganisms:
            self._world.addOrganism(cls(pos, self._world))

    def readInt(self):
        choice = input('> ')
        try:
            n = int(choice)
            return n
        except ValueError:
            return None

    def readClass(self):
        print('Select organism to add')
        for i, org in enumerate(self._knownOrganisms):
            print('{}) {}'.format(i, org.name))
        while True:
            idx = self.readInt()
            if idx is None or idx not in range(len(self._knownOrganisms)):
                print('Not a valid index')
            else:
                break
        print('Selected {}'.format(self._knownOrganisms[idx].name))
        return self._knownOrganisms[idx]


    def readCoord(self, kind, stop):
        print('Choose the {} coordinate'.format(kind))
        while True:
            n = self.readInt()
            if n is None or n not in range(stop):
                print('Not a valid {} coordinate'.format(kind))
            else:
                return n

    def readPosition(self):
        while True:
            x = self.readCoord('x', self._world.width)
            y = self.readCoord('y', self._world.height)
            pos = Position(x, y)
            if self._world.getOrganismFromPosition(pos) is not None:
                print('Position already taken')
            else:
                return pos

    def readOrganism(self):
        cls = self.readClass()
        pos = self.readPosition()
        return cls(pos, self._world)

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            print('\x1b[2J \x1b[H', end='')

    def run(self):
        self.clear()
        print(self._world)

        for _ in range(0, 100):
            print('Press `Enter` for next turn, `a` to add an organism, `q` to quit')
            choice = input('> ').strip()
            if choice == '':
                self.clear()
                self._world.makeTurn()
                for msg in self._world.log:
                    print(msg)
                print(self._world)
            elif choice == 'a':
                org = self.readOrganism()
                self._world.addOrganism(org)
                self.clear()
                print(self._world)
            elif choice == 'q':
                break
            else:
                print("Unknown command")
