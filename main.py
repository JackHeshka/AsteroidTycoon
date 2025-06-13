import math as math
import random as random
import planet as Planet
import player as Pl
import factory as Fc
import station as St
import tradeHub as tHub
## This program would not work without the typing module
from typing import Callable, Dict
## Load data file
import loadData as LD


def use_factory():
    """This used the factory object to let the player use the factorys they have, that is stored station cla"""
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
            print("=" * 80)
            choice = input(f"Enter Number (1-{len(options_list)}): ")
            print("=" * 80)
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
            print("\n")
            print("=" * 80)
            choice = input(f"Enter Number (1-{len(options_list)}): ")
            print("=" * 80)
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
    planet_cost = 500*len(space_player.planets)**2
    while True:
        choice = input(f'This purchase will cost {planet_cost} creadits,' +
                        f' do you wish to proceed? [Y/N]: ').strip().lower()
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
    print("=" * 80)
    new_station.addTile()  # Allow player to add a tile to the station
    

def expand_space_station():
    """This function will allow the player to expand their space station and build factories."""
    new_station.printStation()  # Print the station layout
    print("=" * 80)
    new_station.buyTile(space_player)  # Allow player to expand the station


def exit_game():
    """This function will exit the game."""
    while True:
        try:
            end = input("Would you like to save your station data (y or n):").lower().strip()
            if end == 'y':
                LD.dataSave(space_player, new_station, player_name_txt)
                print("data has been saved")
                break
            elif end == 'n':
                break
        except:
            print("Error Please try again")
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
        print("=" * 80)
        print("You are at the spaces station control center.")
        print("How would you like to proceed?\n")
        options_list = list(game_play_options.keys())
        for index, option in enumerate(options_list, start=1):
            print(f"{index}. {option}")
        print("\n")
        print("=" * 80)
        choice = input(f"Enter Number (1-{len(options_list)}): ")
        print("=" * 80)
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

print("=" * 80)
print("This game is an aventrue based space exploration game. " \
"\nYou will be able to move around the galaxy, explore planets, " \
"\nand gathering resorces from mines. You will then be able to " \
"\ntrade these resources for money, which you can use to build factorys, " \
"\nand expand you spaces station and mining oporation. ")
print("=" * 80)



while True:
    try:
        print("Do you want to load a previous game?")
        choice = input("Enter (yes/no): ").strip().lower()
        print("=" * 80)
        if choice == "no":
        ## for new players, we will create a new player and space station that will later be saved to a file.
            player_name = input("Please create a player name: ")
            player_name_txt = "1" + player_name + ".txt"
            starting_money = 1000  # Set a default starting money value
            space_player = Pl.player(player_name, starting_money)
            new_station = St.spaceStation(player_name)
            new_factory = Fc.Factory()
            new_tradeHub = tHub.tradeHub(new_station)
            break
        elif choice == "yes":
            ## this will load in the players past game, and station layout.
            player_name = input("Please enter your username: ")
            ##Create the file name
            player_name_txt = "1" + player_name + ".txt"
            ##use the laoddata modual to get the info from the the txt file
            player_data, station_data, planet_data = LD.dataLoad(player_name_txt)
            ##Create objects for player and spaceStation
            space_player = Pl.player(player_data["name"], player_data["money"])
            new_station = St.spaceStation(player_data["name"])
            ## Change the base values for the player modual
            space_player.raw_inventory = player_data.get("raw_inventory") or {}
            space_player.refined_inventory = player_data.get("refined_inventory") or {}
            space_player.compound_inventory = player_data.get("compound_inventory") or {}
            space_player.factory_info = player_data.get("factory_info", {})
            space_player.planets = {name: None for name in player_data.get("planets", [])}
            ## change the base values for the station class
            new_station.base_station = station_data.get("base_station", [])
            new_station.tile_in_station = station_data.get("tile_in_station", {})
            new_station.unused_tiles = station_data.get("unused_tiles", {})
            ##Create the factory and tradehub objects
            new_factory = Fc.Factory()
            new_tradeHub = tHub.tradeHub(new_station)
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