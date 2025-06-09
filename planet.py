import math as m
import random as r
import drill as d
from tabulate import tabulate

# Here for out of scope loop breaking
class ScopeBreak(Exception):
    pass

# Main class in this module
class planet:
    planetMap = []
    drills: dict[str, d.drill] = {}
    x = 0
    y = 0

    def __init__(self, name):
        self.name = name
        self.planetMap = self.resourceScatter()
        self.drills = self.initializeDrillVacancy(13, 13)
        self.lowTier = r.choice(["Iron", "Coal", "Copper", "Aluminum"])
        self.midTier = r.choice(["Gold", "Zinc", "Lithium"])
        self.highTier = r.choice(["Diamond", "Lead", "Plutonium"])
        self.userMap = self.initializeUserMap(14,14)

    def __str__(self):
        return self.name
    
    def generateGrid(self, x, y, fill):
        '''
        This function generates a 2-dimensional array based on the height y
        and the width x, fills the values of the array with whatever is passed
        as fill
        '''
        ret = []
        for i in range(0, y):
            ret.append([])
            for j in range(0, x):
                ret[i].append(fill)
        return ret
    
    def initializeUserMap(self, x, y):
        '''
        This function adds a coordinate system to the user map for
        ease of use
        '''
        map = self.generateGrid(x, y, '???')
        # Loops through x and y independently, adding the scales
        for i in range(x):
            map[0][i] = i
        for i in range(y):
            map[i][0] = i
        # Cleans out the (0,0) position, for cleanliness
        map[0][0] = ''
        return map

    def resourceScatter(self):
        '''
            This function will create a 2-dimensional array with
        smooth value blending
            It will add a randomized value between 0 and 1 on every 3rd point
        It will then linearly interpolate (lerp) both horizontally and
        vertically on every 3rd
            And lastly it will average the horizontal and vertical lerp
        for each 1st and 2nd in the x and y directions
        '''
        #Generate base plane
        surface = self.generateGrid(13, 13, None)

        #Random height sample points
        for i in range(int(len(surface)/3)+1):
            for j in range(int(len(surface[i])/3)+1):
                surface[3*i][3*j] = r.random() # type: ignore

        #Linear interpolation
        #Vertical nodes
        for i in range(int(len(surface))):
            segment = i/3
            for j in range(int(len(surface[i])/3)+1):
                try:
                    surface[i][3*j] = self.lerp(surface[3*int(segment)][3*j],
                                            surface[3*(int(segment)+1)][3*j],
                                            segment-int(segment))
                except IndexError: # Defaults to a 50% concentration at edges
                    surface[i][3*j] = self.lerp(surface[3*int(segment)][3*j],
                                            0.5,
                                            segment-int(segment))

        #Horizontal nodes
        for i in range(int(len(surface)/3)+1):
            for j in range(len(surface[i])):
                segment = j/3
                try:
                    surface[3*i][j] = self.lerp(surface[3*i][3*int(segment)],
                                            surface[3*i][3*(int(segment)+1)],
                                            segment-int(segment))
                except IndexError: # Defaults to a 50% concentration at edges
                    surface[3*i][j] = self.lerp(surface[3*i][3*int(segment)],
                                            0.5,
                                            segment-int(segment))
        #Average over the surface
        for i in range(int(len(surface))):
            for j in range(int(len(surface[i]))):
                if surface[i][j] == None:
                    surface[i][j] = (self.lerp(
                        surface[3*round(i/3)][j],
                        surface[3*round(((i+3)/3)-0.5)][j],
                        (i/3) - m.floor(i/3)
                    ) + self.lerp(
                        surface[i][3*round(j/3)],
                        surface[i][3*round(((j+3)/3)-0.5)],
                        (j/3) - m.floor(j/3)
                    ))/2
        return surface
    
    def initializeDrillVacancy(self, x, y):
        '''
        This function generates a dictionary containing each tiles
        vacancy for a drill
        '''
        ret = {}
        for i in range(x):
            for j in range(y):
                ret[f'{i},{j}'] = None
        return ret

    def addDrill(self):
        '''
        This function adds a drill to the current tile if vacant
        '''
        # Update user map
        self.userMap[self.y+1][self.x+1] += '\n(Drilling)'
        if self.drills[f'{self.x},{self.y}'] == None:
            # Add the drill
            self.drills[f'{self.x},{self.y}'] = d.drill(
                                                self.planetMap[self.x][self.y],
                                                self.lowTier, 
                                                self.midTier,
                                                self.highTier
                                                )
            print("Drill placed!")
        else:
            print("There is already a drill there!")

    def groundSurvey(self):
        '''
        This function will add the ore concentration value to
        the user map, and inform the player if it is a good
        spot to mine or not
        '''
        # Convert ore concentration to a percentage
        tile = 100*self.planetMap[self.y][self.x]
        # Update user map
        self.userMap[self.y+1][self.x+1] = f'{round(tile, 1)}%'
        # Give user feedback
        if tile != None:
            if tile > 75:
                print(f'{round(tile, 1)}% Ore Concentration, very good!')
            elif tile > 50:
                print(f'{round(tile, 1)}% Ore Concentration, decent patch.')
            elif tile > 25:
                print(f'{round(tile, 1)}% Ore Concentration, less than ideal.')
            else:
                print(f'{round(tile, 1)}% Ore Concentration, rather awful.')

    def lerp(self, a, b, t):
        '''
        This function is a simple linear interpolation equation
        '''
        return (1-t)*a + t*b
    
    def movePos(self):
        '''
        This function is used to allow the user to select a given tile
        '''
        x_pos = -1
        y_pos = -1
        # Get x from user
        while x_pos > 0 or x_pos <= 14:
            try:
                x_pos = int(input("Please select an x position [1-13]: "))
            except:
                print("Please input an integer")
            if x_pos <= 0 or x_pos > 13:
                print("Please select a number from 1-13 (inclusive)")
            else:
                break
        # Get y from user
        while y_pos > 0 or y_pos <= 14:
            try:
                y_pos = int(input("Please select a y position [1-13]: "))
            except:
                print("Please input an integer")
            if y_pos <= 0 or y_pos > 13:
                print("Please select a number from 1-13 (inclusive)")
            else:
                break
        self.x = x_pos - 1
        self.y = y_pos - 1

    def leavePlanet(self):
        '''
        This function leaves the planet by breaking the planet options loop
        in the main file, raising an error is required to do this so here we
        utilize the ScopeBreak error defined at the top
        '''
        self.x = self.y = 0
        print("Returning to station...")
        raise ScopeBreak
    
    def harvest(self, player):
        '''
        This function will collect all the minerals mined by the drills,
        and display the total to the user
        '''
        total = [0,0,0]
        for key in self.drills.keys():
            if self.drills[key] != None:
                # Mine the resources
                produced = self.drills[key].mine(player) 
                # Track total production
                total[0] += produced[0]
                total[1] += produced[1]
                total[2] += produced[2]
        # Display total accumulated resources
        print('You produced:\n   ' \
             + f'{self.lowTier}: {total[0]}\n   ' \
             + f'{self.midTier}: {total[1]}\n   ' \
             + f'{self.highTier}: {total[2]}')
        
    def displayMap(self):
        '''
        This function will print the user map using the tabulate library
        '''
        print(tabulate(self.userMap))
    
    planetOptions = { # Won't compile without this being at the bottom ¯\_(ツ)_/¯
        "Place Drill": addDrill,
        "Survey Ground": groundSurvey,
        "Move": movePos,
        "Show Map": displayMap,
        "Return to station and harves minerals": leavePlanet
    }