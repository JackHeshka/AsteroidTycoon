class player:
    money = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
        pass

    def __str__(self):
        pass

    def travel(self):
        pass

    def interact(self):
        pass

def get_player_name():
    """
    Prompts the player to input their name and stores it in the player dictionary.
    """
    player["name"] = input("Enter your name: ").strip()
    print(f"Hello, {player['name']}! Welcome to the game.")