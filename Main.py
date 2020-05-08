from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Toadstool import Toadstool
from Organisms.Antelope import Antelope
from Organisms.Alien import Alien
import os

knownOrganisms = [
    Alien,
    Antelope,
    Sheep,
    Wolf,
    Dandelion,
    Grass,
    Toadstool,
]

def readInt():
    choice = input('> ')
    try:
        n = int(choice)
        return n
    except ValueError:
        return None

def readClass():
    print('Select organism to add')
    for i, org in enumerate(knownOrganisms):
        print('{}) {}'.format(i, org.name))
    while True:
        idx = readInt()
        if idx is None or idx not in range(len(knownOrganisms)):
            print('Not a valid index')
        else:
            break
    print('Selected {}'.format(knownOrganisms[idx].name))
    return knownOrganisms[idx]


def readCoord(kind, stop):
    print('Choose the {} coordinate'.format(kind))
    while True:
        n = readInt()
        if n is None or n not in range(stop):
            print('Not a valid {} coordinate'.format(kind))
        else:
            return n

def readPosition(width, height):
    x = readCoord('x', width)
    y = readCoord('y', height)
    return Position(x, y)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        print('\x1b[2J \x1b[H', end='')

if __name__ == '__main__':
    pyWorld = World(8, 8)

    newOrg = Grass(Position(4, 0), pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Sheep(Position(0, 0), pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Dandelion(Position(0, 4), pyWorld)
    pyWorld.addOrganism(newOrg)
    
    newOrg = Wolf(Position(7, 7), pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Toadstool(Position(4, 4), pyWorld)
    pyWorld.addOrganism(newOrg)

    pyWorld.addOrganism(Antelope(Position(6, 7), pyWorld))

    pyWorld.addOrganism(Alien(Position(6, 6), pyWorld))

    clear()
    print(pyWorld)

    for _ in range(0, 100):
        print('Press `Enter` for next turn, `a` to add an organism')
        choice = input('> ')
        if choice == 'a':
            cls = readClass()
            pos = readPosition(pyWorld.width, pyWorld.height)
            pyWorld.addOrganism(cls(pos, pyWorld))
            clear()
            print(pyWorld)
        else:
            clear()
            pyWorld.makeTurn()
            print(pyWorld)
