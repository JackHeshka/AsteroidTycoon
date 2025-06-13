"""This file will reload the playes data based on the text file that has there saved data.

There are some bugs in how this program with the planets and how they store there data, 
to have there data loaded in my me more dificult will solve next day. Will likly use the name
of the planet to initilze the objext, the load the data into that object that is stored after it.
"""

# Kinda bad, moving to pickle in dataHandling.py

import player as Pl
import station as St
import planet as p
import drill as d

baseFile = "baseFileFormat.txt"

def dataLoad(filename):
    """
    Load the playes data from a text file.
    Use inv_section is better to sort through the files in a linear way and
    find what data belongs to what section of the program, reading line by 
    line.

    Planet need to store more data.
    """
    ## values to return
    player_data = {}
    station_data = {}
    planet_data = {}
    ## Track the section in the text file to look at
    section = None
    inv_section = None
    ## open file with given name
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ## find the header PLAYER       
            if line == "PLAYER":
                section = "player"
                inv_section = None
                continue
            ## find the header STATION
            if line == "STATION":
                section = "station"
                inv_section = None
                continue
            if line == "PLANET":
                section = "planet"
                inv_section = None
                continue

                
            ## if the section is player
            if section == "player":
                if line.startswith("name:"):
                    ##Split the line and keep after the :
                    player_data["name"] = line.split(":", 1)[1]
                elif line.startswith("money:"):
                    player_data["money"] = int(line.split(":", 1)[1])
                elif line in ("raw_inventory", "refined_inventory", "compound_inventory"):
                    ## change the inv_section
                    inv_section = line
                    player_data[inv_section] = {}
                elif line == "factory_info:":
                    ## change the inv_section
                    inv_section = "factory_info"
                    player_data["factory_info"] = {}
                elif line == "planets:":
                    ## change the inv_section
                    inv_section = "planets"
                    player_data["planets"] = []
                ## when the inv_section you look at the current line and put that data into that section, and line starts with <
                elif inv_section in ("raw_inventory", "refined_inventory", "compound_inventory") and line.startswith("<"):
                    key, value = line[1:].split(":", 1)
                    player_data[inv_section][key.strip()] = int(value.strip())
                ## store the factroy number and info
                elif inv_section == "factory_info" and ":" in line and "|" in line:
                    ## split the data twice
                    k, rest = line.strip().split(":", 1)
                    num, desc = rest.split("|", 1)
                    player_data["factory_info"][k] = {"num": int(num), "description": desc}

                ## keep track of the planets
                ## This need to be added to because the planets have much more data thn just a name.
                elif inv_section == "planets" and line:
                    player_data["planets"].append(line.strip())

            ## if the section is station
            elif section == "station":
                if line == "base_station:":
                    ## change the inv_section
                    inv_section = "base_station"
                    station_data["base_station"] = []
                elif line == "tile_in_station:":
                    ## change the inv_section
                    inv_section = "tile_in_station"
                    station_data["tile_in_station"] = {}
                elif line == "unused_tiles:":
                    ## change the inv_section
                    inv_section = "unused_tiles"
                    station_data["unused_tiles"] = {}
                elif inv_section == "base_station" and "," in line: # Loads a dictionary
                    ## make row load the data for the text file, by looping through the 
                    # rows and spliting the line at the every , and save the data to row.
                    # split removes leading white space. 
                    row = [int(x) for x in line.strip().split(",")]
                    station_data["base_station"].append(row)
                elif inv_section in ("tile_in_station", "unused_tiles") and ":" in line:
                    k, v = line.strip().split(":")
                    station_data[inv_section][int(k)] = int(v)

            elif section == "planet":
                pass

                
    return player_data, station_data, planet_data

def dataSave(space_player: Pl.player, station: St.spaceStation, filename):
    """
    Saves the player's data to a text file, the data is split into two sections,
    PLAYER, AND STATION. the player section will store all the inventroy data and 
    cretits the player has as well as the planets, Station will store the layout
    of the station and the unused tiles.

    The file will write over the old data if the file has already exists
    """
    ## create a text file and write the player info.
    with open(filename, "w") as f:
        ## header for player info
        f.write(f"PLAYER\n")
        f.write(f"name:{space_player.name}\n")
        f.write(f"money:{space_player.money}\n")
        f.write("raw_inventory\n")
        ## use for loops to write the inventory data
        for k, v in space_player.raw_inventory.items():
            f.write(f"<{k}:{v}\n")
        f.write("refined_inventory\n")
        for k, v in space_player.refined_inventory.items():
            f.write(f"<{k}:{v}\n")
        f.write("compound_inventory\n")
        for k, v in space_player.compound_inventory.items():
            f.write(f"<{k}:{v}\n")
        f.write("factory_info:\n")
        for k, v in space_player.factory_info.items():
            f.write(f"  {k}:{v['num']}|{v['description']}\n")
        ## save the names of the planets the player has, 
        # this is not done need to save more data to work.
        f.write("planets:\n")
        for planet in space_player.planets.keys():
            f.write(f"  {planet}\n")
        ## header for station info
        f.write("\nSTATION\n")
        f.write("base_station:\n")
        ## loop the move through the rows of the map
        for row in station.base_station:
            ## start with spaces
            ## internal loop to move through the data in each 
            # row and add , to seperate
            f.write("  " + ",".join(str(x) for x in row) + "\n")
        ## save the used and unused tiles
        f.write("tile_in_station:\n")
        for k, v in station.tile_in_station.items():
            f.write(f"  {k}:{v}\n")
        f.write("unused_tiles:\n")
        for k, v in station.unused_tiles.items():
            f.write(f"  {k}:{v}\n")
        # Save planet data
        for k, v in p.drills:
            f.write(f"  {k}:{v}\n")
    print(f"Game saved to {filename}")