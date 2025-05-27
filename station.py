baseStation = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 0, 0, 0],
               [0, 2, 1, 3, 1, 1, 5, 0],
               [0, 2, 1, 3, 0, 0, 0, 0],
               [0, 2, 1, 3, 0, 0, 0, 0],
               [0, 0, 0, 5, 0, 0, 0, 0]]

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
        "Cost": 1
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
        "Cost": 0
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
        "Cost": 0
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
        "Cost": 0
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
        "Cost": 0
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
        "Cost": 0
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
        "Cost": 0
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
        "Cost": 0
    }
}
               
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

    def addToStation(self):
        ###This will let the user spend the money that they have made to expand the space station###
        pass

    def removeFromStation(self):
        pass

    def listOfSections(self):
        pass

station = spaceStation()
station.printStation()