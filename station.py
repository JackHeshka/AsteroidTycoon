baseStation = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 0, 0, 0],
               [0, 2, 1, 3, 0, 0, 0, 0],
               [0, 2, 1, 3, 0, 0, 0, 0],
               [0, 2, 1, 3, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]
               
class factory:
    def __init__(self):
        pass

class spaceStation:
    def __init__(self):
        pass

    def printStation(self):
        # Define tile types with their visual representations
        tile_types = {
            0: [
                "**********",
                "**********",
                "**********",
                "**********"],
            1: [
                "+--------+",
                "|        |",
                "|        |",
                "+--------+"],
            2: [
                "+--------+",
                "|  LAB   |",
                "|        |",
                "+--------+"],
            3: [
                "+--------+",
                "|  DOCK  |",
                "|        |",
                "+--------+"],
            # Add more tile types as needed
        }
        for row in baseStation:
            lines = [""] *4
            for col in row:
                cell = tile_types.get(col, tile_types[0])
                for i in range(4):
                    if lines[i]:
                        lines[i] += " "
                    lines[i] += cell[i]
            for line in lines:
                print(line)

    def addToStation(self):
        pass

    def removeFromStation(self):
        pass

station = spaceStation()
station.printStation()