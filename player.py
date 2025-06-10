class player:
    def __init__(self, name: str, starting_money: int):
        self.name: str = name
        self.money: int = int(starting_money)

        self.planets = {}

        self.raw_inventory: dict[str, int] = {"Iron": 2,
                                              "Coal": 0,
                                              "Copper": 3,
                                              "Gold": 0,
                                              "Aluminum": 0,
                                              "Plutonium": 0,
                                              "Zinc": 5,
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
        
        self.factory_info: dict[str, int] = {"Factory 1": {"num":0,
                                                            "description": "Basic refinerys that doubles your input"},
                                                "Factory 2": {"num":0,
                                                            "description": "Advanced refinerys that triples your input"},
                                                "Factory 3": {"num":0,
                                                            "description": "High-tech refinerys that quadruples your input"},   
                                                "Factory 4": {"num":0,
                                                            "description": "Super refinerys that quintuples your input"},
                                                "Factory 5": {"num":0,
                                                            "description": "Mega refinerys that sextuples your input"},
                                                "Factory 6": {"num":0,
                                                            "description": "Ultra refinerys that septuples your input"}}
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
    
    def remove_resource(self,class_type,ore,amount):
        if class_type == "raw_inventory":
            self.raw_inventory[ore] -= amount
        elif class_type == "refined_inventory":
            self.refined_inventory[ore] -= amount
        elif class_type == "compound_inventory":
            self.compound_inventory[ore] -= amount
        else:
            print("Invalid class_type. Must be 'raw', 'refined', or 'compound'.")
            return  


    def print_inventory(self):
        print("Raw Inventory:")
        for item, amount in self.raw_inventory.items():
            print(f"{item}: {amount}")
        print("\nRefined Inventory:")
        for item, amount in self.refined_inventory.items():
            print(f"{item}: {amount}")
        print("\nCompound Inventory:")
        for item, amount in self.compound_inventory.items():
            print(f"{item}: {amount}")
        print("\nFactory Information:")
        for factory, info in self.factory_info.items():
            print(f"{factory} - {info['num']} units: {info['description']}")
        print(f"\nCredits: {self.money}")
        for planet_name, planet in self.planets.items():
            print(f"Planet: {planet_name}, Resources: {planet.get_resources()}")