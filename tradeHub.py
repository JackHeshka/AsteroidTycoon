"""Here is where the player will be able to trade resources to get more money"""
import player as Pl 

price_raw: dict[str, int] = {"Iron": 25,
                              "Coal": 5,
                              "Copper": 40,
                              "Gold": 100,
                              "Aluminum": 20,
                              "Plutonium": 80,
                              "Zinc": 10,
                              "Diamond": 120,
                              "Lead": 30,
                              "Lithium": 80}

price_refined: dict[str, int] = {"Iron": 40,
                                  "Coal": 15,
                                  "Copper": 120,
                                  "Gold": 300,
                                  "Aluminum": 60,
                                  "Plutonium": 240,
                                  "Zinc": 30,
                                  "Diamond": 360,
                                  "Lead": 90,
                                  "Lithium": 240}

price_compound: dict[str, int] = {"Iron": 80,
                                  "Coal": 30,
                                  "Copper": 240,
                                  "Gold": 600,
                                  "Aluminum": 120,
                                  "Plutonium": 480,
                                  "Zinc": 60,
                                  "Diamond": 720,
                                  "Lead": 180,
                                  "Lithium": 480}



class tradeHub:
    def __init__(self, name):
        self.name = name

    def trade_resources(self, space_player: Pl.player):
        """This function will allow the player to trade resources for credits."""
        print("What category of resource would you like to trade?")
        print("1. Raw Resources")
        print("2. Refined Resources")
        print("3. Compounds")
        print("=" * 80)
        try:
            category_choice = input("Enter Number (1-3): ")
            print("=" * 80)
            if category_choice not in ['1', '2', '3']:
                raise ValueError("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            return
        inventory = None
        price_dict = None
        if category_choice == '1':
            print("Here are the raw resources you have collected:\n")
            inventory = space_player.raw_inventory
            price_dict = price_raw
            resource_type = "raw_inventory"
        elif category_choice == '2':
            print("Here are the refined resources you have developed:\n")
            inventory = space_player.refined_inventory
            price_dict = price_refined
            resource_type = "refined_inventory"
        elif category_choice == '3':
            print("Here are the compounds you have created:\n")
            inventory = space_player.compound_inventory
            price_dict = price_compound
            resource_type = "compound_inventory"
        loop = 1
        for player_resource, amount in inventory.items():
            print(f"{loop}. {player_resource} inventory: {amount} (worth {price_dict[player_resource]} credits).")
            loop += 1
        print("\n" + "=" * 80)
        print("Would you like to:")
        print("1. Sell a specific resource")
        print("2. Sell all resources in this category")
        print("=" * 80)
        sell_choice = input("Enter Number (1-2): ")
        print("=" * 80)
 
        if sell_choice == '1':
            try:
                resource_num = int(input("Enter the number of the resource you want to sell: "))
                resource_names = list(inventory)
                if resource_num < 1 or resource_num > len(resource_names):
                    raise IndexError("Invalid resource number.")
                resource_name = resource_names[resource_num - 1]
                if inventory[resource_name] == 0:
                    raise IndexError("You have no units of this resource to sell.")
            except IndexError as e:
                print(f"Error: {e}. Please try again.")

            price = price_dict.get(resource_name, 0)
            total_credits = price * inventory[resource_name]

            print(resource_type)

            print(f"You started with {space_player.money} credits")
            space_player.remove_resource(resource_type, resource_name, total_credits)
            print(f"Sold {inventory[resource_name]} {resource_name} for {total_credits} credits.")
            print(f"You now have {space_player.money} credits")



        elif sell_choice == '2':
            total_credits = 0
            for resource_name, amount in inventory.items():
                price = price_dict.get(resource_name, 0)
                if amount > 0:
                    total_credits = price * amount
                    print(f"Sold {amount} {resource_name} for {price * amount} credits.")
                    space_player.remove_resource(resource_type, resource_name, total_credits)
            print(f"Total credits earned: {total_credits}")
        else:
            print("Invalid choice.")
            

            