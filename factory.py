import station as St

class Factory:
    """Here is where refinement of resources will take place."""
    
    def __init__(self):
        self.factory_types = {
                "Factory 1": {"function": self.factory_1,
                              "numbers": 2,
                              "description": "A place to refine resources into more valuable products.",
                              "required_resources": {"metal_one": None},
                              "change": 5,
                              "output_resources": {"refined_metal": None}},
                "Factory 2": {"function": self.factory_2,
                              "numbers": 0,
                              "description": "Advanced refinery for rare metals.",
                              "required_resources": {"metal_one": None},
                              "change": 5,
                              "output_resources": {"refined_metal": None}},
                "Factory 3": {"function": self.factory_3,
                              "numbers": 0,
                              "description": "High-tech factory for processing complex materials.",
                              "required_resources": {"metal_one": None},
                              "change": 5,
                              "output_resources": {"refined_metal": None}},
                "Factory 4": {"function": self.factory_4,
                                "numbers": 4,
                                "description": "Specialized factory for energy resources.",
                                "required_resources": {"metal_one": None},
                                "change": 5,
                                "output_resources": {"refined_metal": None}},
                "Factory 5": {"function": self.factory_5,
                              "numbers": 0,
                              "description": "Multi-purpose factory for various materials.",
                              "required_resources": {"metal_one": None},
                              "change": 5,
                              "output_resources": {"refined_metal": None}},
                "Factory 6": {"function": self.factory_6,
                              "numbers": 5,
                              "description": "Experimental factory for cutting-edge materials.",
                              "required_resources": {"metal_one": None},
                              "change": 5,
                              "output_resources": {"refined_metal": None}}
        }

    def use_factory(self):
        available = [name for name, f in self.factory_types.items() if f['numbers'] > 0]
        if not available:
            print("No factories available to use.")
            return
        print("Available Factories:")
        for i, name in enumerate(available, 1):
            factory = self.factory_types[name]
            print(f"{i}. You have {factory['numbers']} ({name})")
        while True:
            try:
                choice = int(input("Enter the number of the factory you want to use: "))
                if 1 <= choice <= len(available):
                    selected_name = available[choice - 1]
                    print(f"You selected {selected_name}.")
                    self.factory_types[selected_name]['function']()  # Call the factory function
                    break
                else:
                    print("Invalid selection. Please choose a valid factory number.")
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
        print("You can use these factories to refine resources into more valuable products.")


    def factory_1(self):
        """This function will allow the player to use Factory 1."""
        print("Using Factory 1...")
        # Implement the logic for using Factory 1 here
        # For example, refining resources, updating inventory, etc.
        pass
    def factory_2(self):
        """This function will allow the player to use Factory 2."""
        print("Using Factory 2...")
        # Implement the logic for using Factory 2 here
        # For example, refining resources, updating inventory, etc.
        pass
    def factory_3(self):
        """This function will allow the player to use Factory 3."""
        print("Using Factory 3...")
        # Implement the logic for using Factory 3 here
        # For example, refining resources, updating inventory, etc.
        pass
    def factory_4(self):
        """This function will allow the player to use Factory 4."""
        print("Using Factory 4...")
        # Implement the logic for using Factory 4 here
        # For example, refining resources, updating inventory, etc.
        pass
    def factory_5(self):
        """This function will allow the player to use Factory 5."""
        print("Using Factory 5...")
        # Implement the logic for using Factory 5 here
        # For example, refining resources, updating inventory, etc.
        pass
    def factory_6(self):
        """This function will allow the player to use Factory 6."""
        print("Using Factory 6...")
        # Implement the logic for using Factory 6 here
        # For example, refining resources, updating inventory, etc.
        pass
