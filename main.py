import math as math
import random as random
import planet as Planet
import player as Pl
##import tradeHub as tHub
import factory as Fc
import station as St
import tradeHub as tHub
## This program would not work without the typing module
from typing import Callable, Dict


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
    if not space_player.planets:
        print("You have no planets to visit. Please establish a mining operation first.")
        return
    else:
        while True:
            current_planet = None
            print("Here are the planets you have established mining operations on:")
            options_list = list(space_player.planets.keys())
            for index, option in enumerate(options_list, start=1):
                print(f"{index}. {option}")
            print("================================================================================")
            choice = input(f"Enter Number (1-{len(options_list)}): ")
            print("================================================================================")
            try:
                if choice in map(str, range(1, len(options_list) + 1)):
                    selected_option = options_list[int(choice) - 1]
                    current_planet = space_player.planets[selected_option]
                elif not choice.isdigit():
                    raise ValueError("Enter a Number")
                elif int(choice) not in range(1, len(options_list) + 1):
                    raise ValueError("Choice a Number in range")
            except ValueError as e:
                print(f"Invalid choice. {e}. Error: Please try again.")
            if current_planet != None:
                break
        while True:
            options_list = list(current_planet.planetOptions.keys())
            for index, option in enumerate(options_list, start=1):
                print(f"{index}. {option}")
            print("\n================================================================================")
            choice = input(f"Enter Number (1-{len(options_list)}): ")
            print("================================================================================")
            try:
                if choice in map(str, range(1, len(options_list) + 1)):
                    selected_option = options_list[int(choice) - 1]
                    current_planet.planetOptions[selected_option](current_planet)
                elif not choice.isdigit():
                    raise ValueError("Enter a Number")
                elif int(choice) not in range(1, len(options_list) + 1):
                    raise ValueError("Choice a Number in range")
            except ValueError as e:
                print(f"Invalid choice. {e}. Error: Please try again.")
            except Planet.ScopeBreak:
                current_planet.harvest(space_player)
                break


def establish_mining_operation():
    """This function will allow the player to pick a planet and extract resources from it,
    using a mining function."""
    planet_cost = 500*len(space_player.planets)^2
    while True:
        choice = input(f'This purchase will cost {planet_cost} creadits,\
                        do you wish to proceed? [Y/N]: ').strip().lower()
        if space_player.money >= planet_cost and choice == 'y':
            planet_name = random.choice(list(open('planetNames.txt')))
            while planet_name in space_player.planets.keys():
                planet_name = random.choice(list(open('planetNames.txt')))
            space_player.planets[planet_name] = Planet.planet(planet_name, space_player)
            print(f"\nPurchased mining rights to {space_player.planets[planet_name]}")
            Pl.player.spend_money(space_player, planet_cost)  # Deduct the cost of establishing a mining operation
            print(f"Your current balance is {space_player.money} credits.")
            break
        elif choice == 'n':
            break
        elif space_player.money < planet_cost:
            print('Insufficient funds')
            break
        else:
            print("Something went wrong, please try again")


def trade_resources():
    """This function will allow the player to trade resources they have mined for credits."""
    tHub.tradeHub.trade_resources(new_station, space_player)  # Call the trade resources method


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
    "Use Factory To Refine Resources": use_factory,
    "View Space Station": explore_space_station,
    "View Inventory": player_inventory,
    "Establish Mining Operation": establish_mining_operation,
    "Visit Mining Operations on Planet": visit_planet,
    "Trade Resources": trade_resources,
    "Rebuild Space Station": add_station,
    "Buy Space Station Sections": expand_space_station,
    "Exit Game": exit_game
}


def main_menu():
    """This function displays the main menu and lets the player choose where they want to go in the game."""
    while True:
        print("================================================================================")
        print("You are at the spaces station control center.")
        print("How would you like to proceed?\n")
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
            new_tradeHub = tHub.tradeHub(new_station)
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
print("=" * 80)
print("Loading your space station layout...")
new_station.printStation()  # Print the station layout
print("=" * 80)
print("Welcome to the Space Exploration Game!")
print(f"Commander {space_player.name}, your account balance is {space_player.money} credits.")
print("Your space station is shown above.")
print("=" * 80)
print("Here is the main menu where you can explore the galaxy,")
print("trade resources, and manage your space station.")
print("For the best experience, please expand you termanal window.")
main_menu()  # Start the main menu loop  SS