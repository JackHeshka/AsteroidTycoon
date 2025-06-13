"""This file will reload the playes data based on the text file that has there saved data."""

import player as Pl
import station as St

baseFile = "baseFileFormat.txt"

def dataLoad(filename):
    """
    Load the playes data from a text file.
    Use inv_section is better to sort through the files in a linear way and
    find what data belongs to what section of the program.
    """
    ##values to return
    player_data = {}
    station_data = {}
    ##Track the section in the text file to look at
    section = None
    inv_section = None
    ##open file
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
                    inv_section = "factory_info"
                    player_data["factory_info"] = {}
                elif line == "planets:":
                    inv_section = "planets"
                    player_data["planets"] = []
                ## when the inv_section you look at the current line and put that data into that section, and line starts with <
                elif inv_section in ("raw_inventory", "refined_inventory", "compound_inventory") and line.startswith("<"):
                    key, value = line[1:].split(":", 1)
                    player_data[inv_section][key.strip()] = int(value.strip())
                ## store the factroy number and info
                elif inv_section == "factory_info" and ":" in line and "|" in line:
                    k, rest = line.strip().split(":", 1)
                    num, desc = rest.split("|", 1)
                    player_data["factory_info"][k] = {"num": int(num), "description": desc}
                ## keep track of the planets
                elif inv_section == "planets" and line:
                    player_data["planets"].append(line.strip())

            ## if the section is station
            elif section == "station":
                if line == "base_station:":
                    inv_section = "base_station"
                    station_data["base_station"] = []
                elif line == "tile_in_station:":
                    inv_section = "tile_in_station"
                    station_data["tile_in_station"] = {}
                elif line == "unused_tiles:":
                    inv_section = "unused_tiles"
                    station_data["unused_tiles"] = {}
                elif inv_section == "base_station" and "," in line:
                    row = [int(x) for x in line.strip().split(",")]
                    station_data["base_station"].append(row)
                elif inv_section in ("tile_in_station", "unused_tiles") and ":" in line:
                    k, v = line.strip().split(":")
                    station_data[inv_section][int(k)] = int(v)
    return player_data, station_data

def dataSave(space_player: Pl.player, station: St.spaceStation, filename):
    """
    Saves the player's data and station layout to a text file in a simple format (not JSON).
    """
    with open(filename, "w") as f:
        f.write(f"PLAYER\n")
        f.write(f"name:{space_player.name}\n")
        f.write(f"money:{space_player.money}\n")
        f.write("raw_inventory\n")
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
        f.write("planets:\n")
        for planet in space_player.planets.keys():
            f.write(f"  {planet}\n")
        f.write("\nSTATION\n")
        f.write("base_station:\n")
        for row in station.base_station:
            f.write("  " + ",".join(str(x) for x in row) + "\n")
        f.write("tile_in_station:\n")
        for k, v in station.tile_in_station.items():
            f.write(f"  {k}:{v}\n")
        f.write("unused_tiles:\n")
        for k, v in station.unused_tiles.items():
            f.write(f"  {k}:{v}\n")
    print(f"Game saved to {filename}")