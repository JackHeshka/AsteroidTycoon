"""
This module is used for handling the saving and loading of player data
from past and current sessions
"""
import pickle as pickle
import inspect as inspect
import planet as planet
import player as player
import station as station

def saveData(user:player.player, station:station.spaceStation):
    planet_pkg = {}

    for n, p in user.planets:
        planet_pkg[n] = p

    player_pkg = user

    station_pkg = station

    with open(f"saves\{user.name}_planetData.pkl", 'wb') as file:
        pickle.dump(planet_pkg, file)

    with open(f"saves\{user.name}_playerData.pkl", 'wb') as file:
        pickle.dump(player_pkg, file)

    with open(f"saves\{user.name}_stationData.pkl", 'wb') as file:
        pickle.dump(station_pkg, file)


def loadData(user:str):
    with open(f"saves\{user}_planetData.pkl", 'rb') as file:
        planet_pkg = pickle.load(file)

    with open(f"saves\{user}_playerData.pkl", 'rb') as file:
        player_pkg = pickle.load(file)

    with open(f"saves\{user}_stationData.pkl", 'rb') as file:
        station_pkg = pickle.load(file)

    return [planet_pkg, player_pkg, station_pkg]