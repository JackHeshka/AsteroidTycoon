from typing import List

class player:
    def __init__(self, name: str, starting_money: int):
        self.name: str = name
        self.money: int = int(starting_money)
        self.raw_inventory: dict[str, int] = {"Iron": 0,
                                              "Coal": 0,
                                              "Copper": 0,
                                              "Gold": 0,
                                              "Aluminum": 0,
                                              "Plutonium": 0,
                                              "Zinc": 0,
                                              "Diamond": 0,
                                              "Lead": 0,
                                              "Lithium": 0}

        self.refined_inventory: dict[str, int] = {"Iron": 0,
                                                  "Coal": 0,
                                                  "Copper": 0,
                                                  "Gold": 0,
                                                  "Aluminum": 0,
                                                  "Plutonium": 0,
                                                  "Zinc": 0,
                                                  "Diamond": 0,
                                                  "Lead": 0,
                                                 "Lithium": 0}
        
        self.compound_inventory: dict[str, int] = {"Iron": 0,
                                                   "Coal": 0,
                                                   "Copper": 0,
                                                   "Gold": 0,
                                                   "Aluminum": 0,
                                                   "Plutonium": 0,
                                                   "Zinc": 0,
                                                   "Diamond": 0,
                                                   "Lead": 0,
                                                   "Lithium": 0}

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