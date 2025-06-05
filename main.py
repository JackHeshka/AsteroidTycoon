import math as math
import player as Pl
##import tradeHub as tHub
import factory as Fc
import station as St
## This program would not work without the typing modual
from typing import Callable, Dict

def explore_galaxy():
    """This function will allow the player to explore the planets in the galaxy."""
    print("Exploring the galaxy... (feature coming soon)")

def use_factory():
    """This function will allow the player to use a factory to refine resources."""
    new_factory.use_factory(space_player)  # Call the method to use the factory
 
def explore_space_station():
    """This function will allow the player to explore the space station."""
    new_station.printStation()


def player_inventory():
    """This function will print the player's inventory of resources and credits."""
    Pl.player.print_inventory(space_player)  # Print the player's inventory


def visit_planet():
    """This function will allow the player to pick a planet that they have a mine on and 
    gather the resorces that they have mined while they have been away from the planet."""
    print("Extracting resources... (feature coming soon)")


def establish_mining_operation():
    """This function will allow the player to pick a planet and extract resources from in,
    using a mining function."""
    print("Establishing mining operation... (feature coming soon)")


def trade_resources():
    """This function will allow the player to trade resources they have mined for credits."""
    print("Trading resources... (feature coming soon)")


def add_station():
    """This function will allow the player to build a new space station."""
    new_station.printStation()  # Print the station layout
    print("=================================================================================")
    new_station.addTile()  # Allow player to add a tile to the station
    

def expand_space_station():
    """This function will allow the player to expand their space station and build factories."""
    new_station.printStation()  # Print the station layout
    print("=================================================================================")
    new_station.buyTile(space_player)  # Allow player to expand the station


def exit_game():
    """This function will exit the game."""
    print("Exiting game. Goodbye!")
    exit()


## This dictionary holds the options for the game play menu.
game_play_options: Dict[str, Callable[[], None]] = {
    "Explore Galaxy": explore_galaxy,
    "*Use Factory": use_factory,
    "*Explore Space Station": explore_space_station,
    "Player Inventory": player_inventory,
    "Visit Planet": visit_planet,
    "Establish Mining Operation": establish_mining_operation,
    "Trade Resources": trade_resources,
    "*Build Space Station": add_station,
    "*Buy Space Station Sections": expand_space_station,
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
        choice = input(f"Enter Number (1-{len(options_list)}): ")
        print("================================================================================")
        try:
            if choice in map(str, range(1, len(options_list) + 1)):
                selected_option = options_list[int(choice) - 1]
                game_play_options[selected_option]() ##for later when we have functions for each option:
            elif not choice.isdigit():
                raise ValueError("Enter a Number")
            elif int(choice) not in range(1, len(options_list) + 1):
                raise ValueError("Choice a Number in range")
        except ValueError as e:
            print(f"Invalid choice. {e}. Error: Please try again.")

print("================================================================================")
print("This game is an aventrue based space exploration game. " \
"\nYou will be able to move around the galaxy, explore planets, " \
"\nand gathering resorces from mines. You will then be able to " \
"\ntrade these resources for money, which you can use to build factorys, " \
"\nand expand you spaces station and mining oporation. ")
print("================================================================================")


while True:
    try:
        print("Do you want to load a previous game?")
        choice = input("Enter (yes/no): ").strip().lower()
        print("================================================================================")
        if choice == "no":
        ## for new players, we will create a new player and space station that will later be saved to a file.
            player_name = input("Please create a player name: ")
            starting_money = 1000  # Set a default starting money value
            space_player = Pl.player(player_name, starting_money)
            new_station = St.spaceStation(player_name)
            new_factory = Fc.Factory()
            break
        elif choice == "yes":
            ## this will load in the players past game, and station layout.
            player_name = input("Please enter your username: ")
            station_file = player_name + "_station.txt"
            player_file = player_name + "_player.txt"
            break
        else:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'")
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
print("================================================================================")
print("Loading your space station layout...")
new_station.printStation()  # Print the station layout
print("================================================================================")
print("Welcome to the Space Exploration Game!")
print(f"Commander {space_player.name}, your account balance is {space_player.money} credits.")
print("Your current space station layout is above.")
print("================================================================================")
print("Here is the main menu where you can explore the galaxy,")
print("trade resources, and manage your space station.")
print("For the best experience, please expand you termanal window.")
main_menu()  # Start the main menu loop  SS