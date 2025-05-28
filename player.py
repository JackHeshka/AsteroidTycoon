class player:
    money = 0

    def __init__(self, name, age, station, starting_money):
        self.name = name
        self.age = age
        self.station = station
        self.money = starting_money
        name = input("What is the name of your miner? ")
        age = input("What is your age? ")
        station = input("What will you call your main station")
        pass

    def get_money(self, amount):
        if amount > 0:
            self.money += amount 
            print(f"{self.name} has {amount + self.money} of money left")
        else:
            print("you must add a posative integer")

    def send_money(self, amount):
        if amount < self.money:
            print("you do not have enough money")
        elif amount <= 0:
            print("number must be posative")
        else:
            amount -= self.money
            print(f"{self.name} you have {self.money} dollars left")

    def money_left(self):
        print(f"{self.name} you have {self.money} left")
        return self.money