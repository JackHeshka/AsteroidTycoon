import player as Pl
## This program would not work without the typing modual
from typing import Dict, Any
from typing import List, Optional


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


class factory:
    def __init__(self):
        pass



class spaceStation:
    def __init__(self, name: str):
        self.name = name
        self.tile_in_station = {0: 0,
                                1: 0,
                                2: 0,
                                3: 0,
                                4: 0,
                                5: 0,
                                6: 0,
                                7: 0,
                                8: 0}
        
        self.unused_tiles = {0: 0,
                             1: 0,
                             2: 0,
                             3: 0,
                             4: 0,
                             5: 0,
                             6: 0,
                             7: 0,
                             8: 0}
        
        """ This is the base station layout if the player has played before
        has a profile to load into the game it will be overwritten."""
        self.base_station = [[0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]]

    def loadStation(self, filename: str):
        """This function loads the space station map from a file."""
        station_map: list[list[int]] = []
        with open(filename, 'r') as file:
            for line in file:
                row: list[int] = [int(x) for x in line.strip().split()]
                station_map.append(row)
        self.listOfStationTiles()  # Update the tile counts
        return station_map
    

    def saveStation(self, filename: str):
        """This function saves the space station map to a file."""
        with open(filename, 'w') as file:
            for row in self.base_station:
                file.write(' '.join(str(x) for x in row) + '\n')


    def printStation(self):
        """This function prints the current layout of the space station."""
        print("\n")
        for row in self.base_station:
            lines = [""] * 4
            for col in row:
                cell = tile_types.get(col, tile_types[0])
                for i in range(4):
                    lines[i] += cell["art"][i]
            for line in lines:
                print(line)
        print("\n")


    def buyTile(self, space_player: Pl.player):
        """This function allows the player to add a tile to their space station, by chosing from a list of available tiles."""
        print("You have " + str(space_player.money) + " credits.") ## prints the tile available to the player
        print("Select a tile to buy:")
        print("================================================================================\n")
        for i in range(tile_types.__len__()):
            print(str(i+1) + " - " + tile_types[i]["name"] + " = " + str(tile_types[i]["Cost"]) + " credits")
        print("\n================================================================================")
        while True:
            try:
                choice = int(input("Enter Number: "))
                if choice < 1 or choice > len(tile_types):
                    raise ValueError("Choice must be between 1 and " + str(len(tile_types)))
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
                print("=================================================================================")
        selected_tile = choice - 1
        ## check if the player has enough money to buy the tile
        if selected_tile in tile_types and space_player.money >= tile_types[selected_tile]["Cost"]:
            ## removes the cost of the tile from the player's money
            space_player.spend_money(tile_types[selected_tile]["Cost"])
            print(f"You have bought a {tile_types[selected_tile]['name']}.")
            print(f"Your new balance is {space_player.money} credits.")
            print("=================================================================================")
            ## update the tile count of unused tilesin the station
            self.unused_tiles[selected_tile] += 1
            while True:
                try:
                    print("would you like to add this tile to your space station?")
                    choice = input("Enter (yes/no): ").strip().lower()
                    print("=================================================================================")
                    if choice == "yes":
                        self.add(selected_tile)
                        self.unused_tiles[selected_tile] -= 1
                        break
                    elif choice == "no":
                        print("You can add the tile later.")
                        break
                    else:
                        raise ValueError("Please enter 'yes' or 'no'")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                    return
        else:
            print("Invalid choice or insufficient funds.")


    def addTile(self):
        """this funcion will allow the player to add a tile to their existing space station. it does this
        by checking what spaces are available in the base station and then allowing the player to select"""
        while True:
            try:
                print("How would you like to improve your space station?")
                print("\n1 - Add Unused Tile")
                print("2 - ReBuild Station")
                print("\n=================================================================================")
                choice = input("Enter Number: ")
                print("=================================================================================")

                if choice == "1":
                    """ This will print the unused tiles that the player has."""
                    print("These are your unused tiles:\n")
                elif choice == "2":
                    ## this will clear the base station and retain the tile count to rebuild the station
                    print("Here are all your tiles:\n")
                    self.listOfStationTiles()  # Ensure tile_in_station is up-to-date
                    for i in range(len(self.tile_in_station)):
                        self.unused_tiles[i] += self.tile_in_station[i]  # Add current station tiles to unused
                        self.tile_in_station[i] = 0  # Clear tile_in_station
                    for r in range(len(self.base_station)):
                        for c in range(len(self.base_station[r])):
                            self.base_station[r][c] = 0
                else:
                    raise ValueError("Please enter 1 or 2")
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
            loop = True
            while loop == True:
                available_tiles = [tile_id for tile_id, count in self.unused_tiles.items() if count > 0 and tile_id != 0]
                if available_tiles == []:
                    print("You have no unused tiles to add.")
                    loop = False
                    return
                for idx, tile_id in enumerate(available_tiles, start=1):
                    print(f"{idx}: {tile_types[tile_id]['name']} - {self.unused_tiles[tile_id]} available")
                print("\n=================================================================================")
                try:
                    tile_choice_input = int(input("Enter Number: "))
                    if tile_choice_input <= len(available_tiles):
                        tile_id = available_tiles[tile_choice_input - 1]
                        self.unused_tiles[tile_id] -= 1
                        if choice == "1":
                            loop = False
                        self.add(tile_id)
                    else:
                        raise ValueError("Invalid tile choice or no tiles available.")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
            break  # Exit the loop
            

    def add(self, tile_to_add: int):
        """This function will add a tile to the space station by allowing the player to select a position."""
        numbered_map: List[List[Optional[int]]] = []    ## This will hold the numbered map of the base station
        position_map: dict[int, tuple[int, int]] = {}    ## Maps number to (row, col)
        counter = 1  ## Start numbering from 1 listing the positions
        for r, row_vals in enumerate(self.base_station):
            numbered_row = []
            for c, val in enumerate(row_vals):
                if val == 0:
                    """ If the space is empty, we will add a number to it's position in the map."""
                    numbered_row.append(counter)
                    position_map[counter] = (r, c)
                    counter += 1
                else:
                    numbered_row.append(None)
            numbered_map.append(numbered_row)
        """ Print the station with numbers centered in empty spaces like the other print tile"""
        for row_idx, row in enumerate(self.base_station):
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
                self.base_station[row][col] = tile_to_add
                print(f"Tile placed at ({row}, {col}).")
                self.printStation()
        except ValueError:
            print("Invalid input. Please enter a number.")


    def redueStation(self):
        pass


    def removeFromStation(self):
        pass


    def listOfStationTiles(self):
        """This function will create a list of all the tiles that the spaces station has to use."""
        for row in self.base_station:
            for type in row:
                self.tile_in_station[type] += 1
  

    def addToStation(self, space_player:Pl.player):
        pass