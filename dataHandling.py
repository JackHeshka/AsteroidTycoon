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
    player_pkg = user
    station_pkg = station

    try:
        with open(f"saves\\{user.name.lower()}_playerData.pkl", 'wb') as file:
            pickle.dump(player_pkg, file)

        with open(f"saves\\{user.name.lower()}_stationData.pkl", 'wb') as file:
            pickle.dump(station_pkg, file)
    except:
        print("Something went wrong")


def loadData(user:str):
    user = user.lower()
    
    with open(f"saves\\{user}_planetData.pkl", 'rb') as file:
        planet_pkg = pickle.load(file)

    with open(f"saves\\{user}_stationData.pkl", 'rb') as file:
        station_pkg = pickle.load(file)

    return [planet_pkg, station_pkg]


def newUser(user:str):
    setup = []
    user = user.lower()
    while True:
        try:
            with open(f"saves\\userLog.pkl", 'rb') as file:
                users:list = pickle.load(file)
                users.append(user.lower())
            with open(f"saves\\userLog.pkl", 'wb') as file:
                pickle.dump(users, file)
            break
        except EOFError:
            with open(f"saves\\userLog.pkl", 'wb') as file:
                pickle.dump(setup, file)


def wipeUserLog():
    with open(f"saves\\userLog.pkl", 'wb') as file:
        pickle.dump(None, file)
        pickle.dump([], file)


def getUserLog():
    try:
        with open(f"saves\\userLog.pkl", 'rb') as file:
            return pickle.load(file)
    except EOFError as e:
        wipeUserLog()
        exit(f'Save data has been corrupted (Error: {e})')