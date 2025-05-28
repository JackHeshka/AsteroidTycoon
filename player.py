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

    def buy(self):


        pass

    def interact(self):
        pass