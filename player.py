class player:
    def __init__(self, name, starting_money):
        self.name = name
        self.money = starting_money
        self.inventory = []
        self.health = 100
        
        
    def get_money(self, amount):
        if amount > 0:
            self.money += amount 
        else:
            print("you must add a posative integer")

    def spend_money(self, amount):
        if amount < self.money:
            print("you do not have enough money")
        elif amount <= 0:
            print("number must be posative")
        else:
            amount -= self.money

    def money_left(self):
        return self.money