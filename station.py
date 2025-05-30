import player as Pl

baseStation = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 2, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

from typing import Dict, Any

tile_types: Dict[int, Dict[str, Any]] = {
    0: {
        "art": [
            "**********",
            "**********",
            "**********",
            "**********"
        ],
        "name": "space",
        "description": "Impassable wall section.",
        "Cost": 0
    },
    1: {
        "art": [
            "+--------+",
            "|        |",
            "|        |",
            "+--------+"
        ],
        "name": "Hallway",
        "description": "A simple corridor.",
        "Cost": 10
    },
    2: {
        "art": [
            "+--------+",
            "|  LAB   |",
            "|        |",
            "+--------+"
        ],
        "name": "Lab",
        "description": "Science laboratory.",
        "Cost": 30
    },
    3: {
        "art": [
            "+--------+",
            "|  DOCK  |",
            "|        |",
            "+--------+"
        ],
        "name": "Dock",
        "description": "Spaceship docking bay.",
        "Cost": 20
    },
    4: {
        "art": [
            "+--------+",
            "| Sleep  |",
            "|        |",
            "+--------+"
        ],
        "name": "Sleeping Quarters",
        "description": "Crew sleeping area.",
        "Cost": 40
    },
    5: {
        "art": [
            "+--------+",
            "|Factory |",
            "|  1     |",
            "+--------+"
        ],
        "name": "Factory",
        "description": "Manufacturing facility One.",
        "Cost": 60
    },
    6: {
        "art": [
            "+--------+",
            "|Factory |",
            "|  2     |",
            "+--------+"
        ],
        "name": "Factory",
        "description": "Manufacturing facility Two.",
        "Cost": 60
    },
    7: {
        "art": [
            "+--------+",
            "|Factory |",
            "|  3     |",
            "+--------+"
        ],
        "name": "Factory",
        "description": "Manufacturing facility Three.",
        "Cost": 60
    },
    8: {
        "art": [
            "+--------+",
            "|Factory |",
            "|  4     |",
            "+--------+"
        ],
        "name": "Factory",
        "description": "Manufacturing facility Four.",
        "Cost": 60
    }
}

def load_station_map(filename: str):
###this will load in to the program the map that is stroed into the syatem at the start of the game
    station_map: list[list[int]] = []
    with open(filename, 'r') as file:
        for line in file:
            row: list[int] = [int(x) for x in line.strip().split()]
            station_map.append(row)
    return station_map
               
class factory:
    def __init__(self):
        pass

class spaceStation:
    def __init__(self):
        pass

    def printStation(self):
    ###Prints the space station layout in a readable format.###
        for row in baseStation:
            lines = [""] * 4
            for col in row:
                cell = tile_types.get(col, tile_types[0])
                for i in range(4):
                    lines[i] += cell["art"][i]
            for line in lines:
                print(line)

    def addToStation(self, space_player:Pl.player):
        ###This will let the user spend the money that they have made to expand the space station###
        print("You have " + str(space_player.money) + "credits .")

    def removeFromStation(self):
        pass

    def listOfSections(self):
        pass