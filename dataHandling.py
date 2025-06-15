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
    '''
    This function will save the current game data
    to a designated serialized file
    '''
    # Saves the given player and station data
    try:
        with open(f"saves\\{user.name.lower()}_playerData.pkl", 'wb') as file:
            pickle.dump(user, file)

        with open(f"saves\\{user.name.lower()}_stationData.pkl", 'wb') as file:
            pickle.dump(station, file)
    # If something happens, let the user know
    except:
        print("Something went wrong")


def loadData(user:str):
    '''
    This function will deserialize past game data and return it
    '''
    user = user.lower() # For easy file sorting
    # Loads player data
    with open(f"saves\\{user}_playerData.pkl", 'rb') as file:
        player_pkg = pickle.load(file)
    # Loads station data
    with open(f"saves\\{user}_stationData.pkl", 'rb') as file:
        station_pkg = pickle.load(file)
    # Return both sets of data
    return [player_pkg, station_pkg]


def newUser(user:str):
    '''
    This function will add a new user to the user log
    '''
    user = user.lower()
    while True:
        try:
            # Opens user log and appends the new user
            with open(f"saves\\userLog.pkl", 'rb') as file:
                users:list = pickle.load(file)
                users.append(user.lower())
            # Repackages the updated user log and saves it
            with open(f"saves\\userLog.pkl", 'wb') as file:
                pickle.dump(users, file)
            break
        # If the user log is corrupted, it gets wiped and reset
        except EOFError:
            wipeUserLog()


def wipeUserLog():
    '''
    This function wipes all data of past users
    '''
    with open(f"saves\\userLog.pkl", 'wb') as file:
        pickle.dump([], file)


def getUserLog() -> list:
    '''
    This function returns the user log
    '''
    while True:
        try:
            # Opens user log
            with open(f"saves\\userLog.pkl", 'rb') as file:
                return pickle.load(file)
        # If the user log is corrupted, it gets wiped and reset
        except EOFError as e:
            wipeUserLog()