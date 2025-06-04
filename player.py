from typing import List

class player:
    def __init__(self, name: str, starting_money: int):
        self.name: str = name
        self.money: int = int(starting_money)
        self.inventory: List[str] = []
        self.health: int = 100

    def get_money(self, amount: int):
        if amount > 0:
            self.money += amount 
        else:
            print("you must add a positive integer")

    def spend_money(self, amount: int):
        if amount > self.money:
            print("you do not have enough money")
        elif amount <= 0:
            print("number must be positive")
        else:
            self.money -= amount

    def money_left(self):
        return self.money