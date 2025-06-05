import player as Pl

class Factory:
    """Here is where refinement of resources will take place."""
    
    def __init__(self):
        pass

    def use_factory(self, space_player: Pl.player):
        """This function will allow the player to pick which factory to refine resources in."""
        print("Here are the factories you can use:\n")
        inx = 1 # number to display for user input
        for factory_name, factory_data in space_player.factory_info.items():
            if factory_data["num"] > 0:
                print(f"{inx}. You have {factory_data['num']}: {factory_data['description']}")
                inx += 1
        print("\n================================================================================")
        available_factories = [] # this list will hold the names of the factories that the player has available to use
        for factory_name, factory_data in space_player.factory_info.items():
            if factory_data["num"] > 0:
                available_factories.append(factory_name)
        if not available_factories: # if the player has no factories available
            print("You do not own any factories to use.")
            return
        while True:
            try:
                choice = input("Enter the number of the factory you want to use: ")
                if not choice.isdigit():
                    raise ValueError("Input must be a number")
                choice = int(choice)
                if 1 <= choice <= len(available_factories):
                    selected_factory = available_factories[choice - 1]
                    if selected_factory == "Factory 1":
                        self.factory_1(space_player)
                        break
                    elif selected_factory == "Factory 2":
                        self.factory_2(space_player)
                        break
                    elif selected_factory == "Factory 3":
                        self.factory_3(space_player)
                        break
                    elif selected_factory == "Factory 4":
                        self.factory_4(space_player)
                        break
                    elif selected_factory == "Factory 5":
                        self.factory_5(space_player)
                        break
                    elif selected_factory == "Factory 6":
                        self.factory_6(space_player)
                        break
                else:
                    raise ValueError("Invalid number.")
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
                print("================================================================================")

    def factory_1(self, space_player: Pl.player):
        """This function will allow the player to use Factory 1, to double their input."""
        print(space_player.factory_info["Factory 1"]["description"]+"\n")
        available_resources = []
        inx = 1
        for r in space_player.raw_inventory:
            if space_player.raw_inventory[r] > 0: # Check if the player has any of this resource
                available_resources.append(r)
                print(f"{inx}. {r} - {space_player.raw_inventory[r]} units")
                inx += 1
        print("\n================================================================================")
        if available_resources == []:
            print("You do not have any resources to refine.")
            return
        else:
            while True:
                try:
                    choice = int(input("Enter the number of the resource you want to refine: "))
                    if 1 <= choice <= len(available_resources):
                        selected_resource = available_resources[choice - 1]
                        amount = int(input(f"How many units of {selected_resource} do you want to refine? "))
                        if amount <= 0:
                            raise ValueError("Amount must be positive.")
                        if amount > space_player.raw_inventory[selected_resource]:
                            raise ValueError("You do not have enough of that resource.")
                        # Perform refinement
                        refined_amount = amount * 2  # Factory 1 doubles the input
                        space_player.raw_inventory[selected_resource] -= amount # Reduce raw inventory
                        space_player.refined_inventory[selected_resource] += refined_amount # Add to refined inventory
                        print(f"Refined {amount} units of {selected_resource} into {refined_amount} units of refined {selected_resource}.")
                        break
                    else:
                        raise ValueError("Invalid number")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                    print("================================================================================")
    
    def factory_2(self, space_player: Pl.player):
        """This function will allow the player to use Factory 2."""
        print(space_player.factory_info["Factory 2"]["description"]+"\n")
        available_resources = []
        inx = 1
        for r in space_player.raw_inventory:
            if space_player.raw_inventory[r] > 0: # Check if the player has any of this resource
                available_resources.append(r)
                print(f"{inx}. {r} - {space_player.raw_inventory[r]} units")
                inx += 1
        print("\n================================================================================")
        if available_resources == []:
            print("You do not have any resources to refine.")
            return
        else:
            while True:
                try:
                    choice = int(input("Enter the number of the resource you want to refine: "))
                    if 1 <= choice <= len(available_resources):
                        selected_resource = available_resources[choice - 1]
                        amount = int(input(f"How many units of {selected_resource} do you want to refine? "))
                        if amount <= 0:
                            raise ValueError("Amount must be positive.")
                        if amount > space_player.raw_inventory[selected_resource]:
                            raise ValueError("You do not have enough of that resource.")
                        # Perform refinement
                        refined_amount = amount * 3  # Factory 1 doubles the input
                        space_player.raw_inventory[selected_resource] -= amount # Reduce raw inventory
                        space_player.refined_inventory[selected_resource] += refined_amount # Add to refined inventory
                        print(f"Refined {amount} units of {selected_resource} into {refined_amount} units of refined {selected_resource}.")
                        break
                    else:
                        raise ValueError("Invalid number")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                    print("================================================================================")

    def factory_3(self, space_player: Pl.player):
        """This function will allow the player to use Factory 3."""
        print(space_player.factory_info["Factory 3"]["description"]+"\n")
        available_resources = []
        inx = 1
        for r in space_player.raw_inventory:
            if space_player.raw_inventory[r] > 0: # Check if the player has any of this resource
                available_resources.append(r)
                print(f"{inx}. {r} - {space_player.raw_inventory[r]} units")
                inx += 1
        print("\n================================================================================")
        if available_resources == []:
            print("You do not have any resources to refine.")
            return
        else:
            while True:
                try:
                    choice = int(input("Enter the number of the resource you want to refine: "))
                    if 1 <= choice <= len(available_resources):
                        selected_resource = available_resources[choice - 1]
                        amount = int(input(f"How many units of {selected_resource} do you want to refine? "))
                        if amount <= 0:
                            raise ValueError("Amount must be positive.")
                        if amount > space_player.raw_inventory[selected_resource]:
                            raise ValueError("You do not have enough of that resource.")
                        # Perform refinement
                        refined_amount = amount * 4  # Factory 1 doubles the input
                        space_player.raw_inventory[selected_resource] -= amount # Reduce raw inventory
                        space_player.refined_inventory[selected_resource] += refined_amount # Add to refined inventory
                        print(f"Refined {amount} units of {selected_resource} into {refined_amount} units of refined {selected_resource}.")
                        break
                    else:
                        raise ValueError("Invalid number")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                    print("================================================================================")

    def factory_4(self, space_player: Pl.player):
        """This function will allow the player to use Factory 4."""
        print(space_player.factory_info["Factory 4"]["description"]+"\n")
        available_resources = []
        inx = 1
        for r in space_player.raw_inventory:
            if space_player.raw_inventory[r] > 0: # Check if the player has any of this resource
                available_resources.append(r)
                print(f"{inx}. {r} - {space_player.raw_inventory[r]} units")
                inx += 1
        print("\n================================================================================")
        if available_resources == []:
            print("You do not have any resources to refine.")
            return
        else:
            while True:
                try:
                    choice = int(input("Enter the number of the resource you want to refine: "))
                    if 1 <= choice <= len(available_resources):
                        selected_resource = available_resources[choice - 1]
                        amount = int(input(f"How many units of {selected_resource} do you want to refine? "))
                        if amount <= 0:
                            raise ValueError("Amount must be positive.")
                        if amount > space_player.raw_inventory[selected_resource]:
                            raise ValueError("You do not have enough of that resource.")
                        # Perform refinement
                        refined_amount = amount * 5  # Factory 1 doubles the input
                        space_player.raw_inventory[selected_resource] -= amount # Reduce raw inventory
                        space_player.refined_inventory[selected_resource] += refined_amount # Add to refined inventory
                        print(f"Refined {amount} units of {selected_resource} into {refined_amount} units of refined {selected_resource}.")
                        break
                    else:
                        raise ValueError("Invalid number")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                    print("================================================================================")

    def factory_5(self, space_player: Pl.player):
        """This function will allow the player to use Factory 5."""
        print(space_player.factory_info["Factory 5"]["description"]+"\n")
        available_resources = []
        inx = 1
        for r in space_player.raw_inventory:
            if space_player.raw_inventory[r] > 0: # Check if the player has any of this resource
                available_resources.append(r)
                print(f"{inx}. {r} - {space_player.raw_inventory[r]} units")
                inx += 1
        print("\n================================================================================")
        if available_resources == []:
            print("You do not have any resources to refine.")
            return
        else:
            while True:
                try:
                    choice = int(input("Enter the number of the resource you want to refine: "))
                    if 1 <= choice <= len(available_resources):
                        selected_resource = available_resources[choice - 1]
                        amount = int(input(f"How many units of {selected_resource} do you want to refine? "))
                        if amount <= 0:
                            raise ValueError("Amount must be positive.")
                        if amount > space_player.raw_inventory[selected_resource]:
                            raise ValueError("You do not have enough of that resource.")
                        # Perform refinement
                        refined_amount = amount * 6  # Factory 1 doubles the input
                        space_player.raw_inventory[selected_resource] -= amount # Reduce raw inventory
                        space_player.refined_inventory[selected_resource] += refined_amount # Add to refined inventory
                        print(f"Refined {amount} units of {selected_resource} into {refined_amount} units of refined {selected_resource}.")
                        break
                    else:
                        raise ValueError("Invalid number")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                    print("================================================================================")

    def factory_6(self, space_player: Pl.player):
        """This function will allow the player to use Factory 6."""
        print(space_player.factory_info["Factory 2"]["description"]+"\n")
        available_resources = []
        inx = 1
        for r in space_player.refined_inventory:
            if space_player.refined_inventory[r] > 0: # Check if the player has any of this resource
                available_resources.append(r)
                print(f"{inx}. {r} - {space_player.refined_inventory[r]} units")
                inx += 1
        print("\n================================================================================")
        if available_resources == []:
            print("You do not have any resources to refine.")
            return
        else:
            while True:
                try:
                    choice = int(input("Enter the number of the resource you want to refine: "))
                    if 1 <= choice <= len(available_resources):
                        selected_resource = available_resources[choice - 1]
                        amount = int(input(f"How many units of {selected_resource} do you want to refine? "))
                        if amount <= 0:
                            raise ValueError("Amount must be positive.")
                        if amount > space_player.refined_inventory[selected_resource]:
                            raise ValueError("You do not have enough of that resource.")
                        # Perform refinement
                        refined_amount = amount * 7  # Factory 1 doubles the input
                        space_player.refined_inventory[selected_resource] -= amount # Reduce raw inventory
                        space_player.compound_inventory[selected_resource] += refined_amount # Add to refined inventory
                        print(f"Refined {amount} units of {selected_resource} into {refined_amount} units of refined {selected_resource}.")
                        break
                    else:
                        raise ValueError("Invalid number")
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
                    print("================================================================================")