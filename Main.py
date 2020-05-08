from Game import Game
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Toadstool import Toadstool
from Organisms.Antelope import Antelope
from Organisms.Alien import Alien

def main():
    knownOrganisms = [
        Alien,
        Antelope,
        Sheep,
        Wolf,
        Dandelion,
        Grass,
        Toadstool,
    ]
    startingOrganisms = [
        (Grass, Position(4, 0)),
        (Sheep, Position(0, 0)),
        (Dandelion, Position(0, 4)),
        (Wolf, Position(7, 7)),
        (Toadstool, Position(4, 4)),
        (Antelope, Position(6, 7)),
        (Alien, Position(6, 6)),
    ]
    game = Game(8, 8, knownOrganisms, startingOrganisms)
    game.run()

if __name__ == '__main__':
    main()
