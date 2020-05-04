from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Toadstool import Toadstool
from Organisms.Antelope import Antelope
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        print('\x1b[2J \x1b[H', end='')

if __name__ == '__main__':
    pyWorld = World(8, 8)

    newOrg = Grass(position=Position(xPosition=4, yPosition=0), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Sheep(position=Position(xPosition=0, yPosition=0), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Dandelion(position=Position(xPosition=0, yPosition=4), world=pyWorld)
    pyWorld.addOrganism(newOrg)
    
    newOrg = Wolf(position=Position(xPosition=7, yPosition=7), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Toadstool(position=Position(xPosition=4, yPosition=4), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    pyWorld.addOrganism(Antelope(position=Position(xPosition=6, yPosition=7), world=pyWorld))

    clear()
    print(pyWorld)

    for _ in range(0, 100):
        input('')
        clear()
        pyWorld.makeTurn()
        print(pyWorld)
