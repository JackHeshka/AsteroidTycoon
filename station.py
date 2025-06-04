import player as Pl
## This program would not work without the typing modual
from typing import Dict, Any
from typing import List, Optional
""" This is the base station layout if the player has played before
has a profile to load into the game it will be overwritten."""
baseStation = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 2, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
""" This is the types of tiles that you can place
and can be used ot build the space station."""
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
        "name": "Factory 1",
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
        "name": "Factory 2",
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
        "name": "Factory 3",
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
        "name": "Factory 4",
        "description": "Manufacturing facility Four.",
        "Cost": 1100
    }
}


def load_station_map(filename: str):
    """This function loads the space station map from a file."""
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
        self.tile_in_station = {0: 0,
                                1: 0,
                                2: 0,
                                3: 0,
                                4: 0,
                                5: 0,
                                6: 0,
                                7: 0,
                                8: 0}

    def printStation(self):
        """This function prints the current layout of the space station."""
        print("\n")
        for row in baseStation:
            lines = [""] * 4
            for col in row:
                cell = tile_types.get(col, tile_types[0])
                for i in range(4):
                    lines[i] += cell["art"][i]
            for line in lines:
                print(line)
        print("\n")

    def addToStation(self, space_player:Pl.player):
        """This function allows the player to add a tile to their space station."""
        ## prints the tile available to the player
        print("You have " + str(space_player.money) + " credits.")
        print("Select the tile type you would like to add to your space station.")
        print("================================================================================\n")
        for i in range(tile_types.__len__()):
            print(str(i+1) + " - " + tile_types[i]["name"] + " = " + str(tile_types[i]["Cost"]) + " credits")
        print("\n================================================================================")
        choice = int(input("Enter the tile you want to add: "))
        print("================================================================================")
        selected_tile = choice - 1
        ## chechs if the player has enough money to buy the tile
        if selected_tile in tile_types and space_player.money >= tile_types[selected_tile]["Cost"]:
            ## removes the cost of the tile from the player's money
            space_player.spend_money(tile_types[selected_tile]["Cost"])
            print(f"You have bought a {tile_types[selected_tile]['name']}.")
            print(f"Your new balance is {space_player.money} credits.")
            self.addtile(selected_tile)
        else:
            print("Invalid choice or insufficient funds.")

    def addtile(self, selected_tile):
        """This function allows the player to select a location for the tile."""
        print("Where would you like to place it?")
        print("================================================================================\n")
        """I was having issues with the types giving me errors this is a workarounds that worked for me."""
        numbered_map: List[List[Optional[int]]] = []
        position_map: dict[int, tuple[int, int]] = {}  ## Maps number to (row, col)
        counter = 1 ## Start numbering from 1 listing the positions
        for r, row_vals in enumerate(baseStation):
            numbered_row: List[Optional[int]] = []
            for c, val in enumerate(row_vals):
                if val == 0:
                    numbered_row.append(counter)
                    position_map[counter] = (r, c)
                    counter += 1
                else:
                    numbered_row.append(None)
            numbered_map.append(numbered_row)

        ## Print the station with numbers centered in empty spaces like the other print tile
        ##print("\nSelect a position to place your tile:")
        for row_idx, row in enumerate(baseStation):
            lines = [""] * 4
            for col_idx, col in enumerate(row):
                cell = tile_types.get(col, tile_types[0])
                if col == 0 and numbered_map[row_idx][col_idx] is not None:
                    num_str = str(numbered_map[row_idx][col_idx])
                    # Center the number in the art
                    art = [
                        "**********",
                        "*{:^8s}*".format(num_str),
                        "**********",
                        "**********"
                    ]
                else:
                    art = cell["art"]
                for i in range(4):
                    lines[i] += art[i]
            for line in lines:
                print(line)
        print("\n================================================================================")
        try:
            pos_choice = int(input("Enter the number of the position to place your tile: "))
            if pos_choice in position_map:
                row, col = position_map[pos_choice]
                ## adds the tile to the base station 
                baseStation[row][col] = selected_tile
                print(f"Tile placed at ({row}, {col}).")
                self.printStation()
        except ValueError:
            print("Invalid input. Please enter a number.")


    def removeFromStation(self):
        pass

    def listOfSections(self):
        """This function will create a list of all the tiles that the spaces station has to use."""
        for row in baseStation:
            for type in row:
                self.tile_in_station[type] += 1
        print(self.tile_in_station)

            