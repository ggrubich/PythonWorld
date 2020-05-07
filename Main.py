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
        input('')
        clear()
        pyWorld.makeTurn()
        print(pyWorld)
