import math as math
import factory
import miner
import planet
import player
import galaxy
import station as station

print("======================================================================")
print("This game is an aventrue based space exploration game. " \
"\nYou will be able to move around the galaxy, explore planets, " \
"\nand gathering resorces from mines. You will then be able to " \
"\ntrade these resources for money, which you can use to build factorys, " \
"\nand expand you spaces station and mining oporation. ")
print("======================================================================\n")

game_play_options = {"Explore Galaxy": None,
                     "Explore Space Station": None,
                     "Player Inventory": None,
                     "Extract Resources": None,
                     "Establish Mining Operation": None,
                     "Trade Resources": None, 
                     "Build Factory": None,
                     "Expand Space Station": None,
                     "Upgrade Ship": None,
                     "Exit Game": None}

def load_station_map(filename):
    station_map = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            station_map.append(row)
    return station_map

# Usage:
baseStation = load_station_map('station_map.txt')

def main_menu():
    while True:
        print("Welcome to the Space Exploration Game!")
        print("Please select an option from the menu below:")
        print("\n======================================================================\n")

        for index, option in enumerate(game_play_options.keys(), start=1):
            print(f"{index}. {option}")

        print("\n======================================================================")
        choice = input("Select an option (1-{}): ".format(len(game_play_options)))
        print("======================================================================\n")
        try:
            if choice in map(str, range(1, len(game_play_options) + 1)):
                selected_option = list(game_play_options.keys())[int(choice) - 1]
                print(f"You selected: {selected_option}")
                ##game_play_options[selected_option]() ##for later when we have functions for each option:
            elif not choice.isdigit():
                raise ValueError("Choice is not a number.")
            elif choice not in range(1, len(game_play_options) + 1):
                raise ValueError("Choice not in valid range.")
        
        except ValueError as e:
            print(f"Invalid choice. {e}")
            print("======================================================================\n")

main_menu()