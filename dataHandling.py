"""
This module is used for handling the saving and loading of player data
from past and current sessions
"""
import pickle as pickle
import planet as planet
import player as player
import station as station

def saveData(user:player.player):
    planet_pkg = {}
    player_pkg = {}
    station_pkg = {}

    for n, p in user.planets:
        planet_pkg[n] = p

    with open(f"saves\{user.name}_planetData.pkl", 'wb') as file:
        pickle.dump(planet_pkg, file)

    with open(f"saves\{user.name}_playerDat.pkl", 'wb') as file:
        pickle.dump(player_pkg, file)

    with open(f"saves\{user.name}_stationDat.pkl", 'wb') as file:
        pickle.dump(station_pkg, file)


def loadData():
    pass