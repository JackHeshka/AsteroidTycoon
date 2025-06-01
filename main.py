import math as math
## import factory
## import miner
## import planet
import player as Pl
## import galaxy
import station as St
## This program would not work without the typing modual
from typing import Callable, Dict

print("================================================================================")
print("This game is an aventrue based space exploration game. " \
"\nYou will be able to move around the galaxy, explore planets, " \
"\nand gathering resorces from mines. You will then be able to " \
"\ntrade these resources for money, which you can use to build factorys, " \
"\nand expand you spaces station and mining oporation. ")
print("================================================================================")


def explore_galaxy():
    """This function will allow the player to explore the planets in the galaxy."""
    print("Exploring the galaxy... (feature coming soon)")


def explore_space_station():
    """This function will allow the player to explore the space station."""
    new_station.printStation()


def player_inventory():
    """This function will print the player's inventory of resources and credits."""
    print("Viewing player inventory... (feature coming soon)")


def extract_resources():
    """This function will allow the player to pick a planet that they have a mine on and 
    gather the resorces that they have mined well they have been away from the planet."""
    print("Extracting resources... (feature coming soon)")


def establish_mining_operation():
    """This function will allow the player to pick a planet and extract resources from in,
    using a mining function."""
    print("Establishing mining operation... (feature coming soon)")


def trade_resources():
    """This function will allow the player to trade resources they have mined for credits."""
    print("Trading resources... (feature coming soon)")


def use_factory():
    """This function will allow the player to use a factory that they have built before,
    to build products that they can then trade for more credits than the raw resource."""
    print("Building factory... (feature coming soon)")


def expand_space_station():
    """This function will allow the player to expand their space station and build factories."""
    new_station.printStation()  # Print the station layout
    print("=================================================================================")
    new_station.addToStation(space_player)  # Allow player to expand the station


def exit_game():
    """This function will exit the game."""
    print("Exiting game. Goodbye!")
    exit()


## This dictionary holds the options for the game play menu.
game_play_options: Dict[str, Callable[[], None]] = {
    "Explore Galaxy": explore_galaxy,
    "Explore Space Station": explore_space_station,
    "Player Inventory": player_inventory,
    "Extract Resources": extract_resources,
    "Establish Mining Operation": establish_mining_operation,
    "Trade Resources": trade_resources,
    "Build Factory": use_factory,
    "Expand Space Station": expand_space_station,
    "Exit Game": exit_game
}


def main_menu():
    """This function displays the main menu and lets the player choose where they want to go in the game."""
    while True:
        print("================================================================================\n")
        options_list = list(game_play_options.keys())
        for index, option in enumerate(options_list, start=1):
            print(f"{index}. {option}")
        print("\n================================================================================")
        choice = input("Select an option (1-{}): ".format(len(options_list)))
        print("================================================================================")
        try:
            if choice in map(str, range(1, len(options_list) + 1)):
                selected_option = options_list[int(choice) - 1]
                game_play_options[selected_option]() ##for later when we have functions for each option:
            elif not choice.isdigit():
                raise ValueError("Choice is not a number.")
            elif int(choice) not in range(1, len(options_list) + 1):
                raise ValueError("Choice not in valid range.")
        except ValueError as e:
            print(f"Invalid choice. {e}")
            print("================================================================================\n")


## Main game initialization lets the player enter their name and sets up the space station.
player_name = input("Enter your player name: ")
space_player = Pl.player(player_name, 1000)
## Create a new space station instance
new_station = St.spaceStation()
St.baseStation = St.load_station_map('station_map.txt')
print("================================================================================")
print("Loading your space station layout...")
new_station.printStation()  # Print the station layout
print("================================================================================")
print("Welcome to the Space Exploration Game!")
print(f"Commander {space_player.name}, your account balance is {space_player.money:,} credits.")
main_menu()  # Start the main menu loop