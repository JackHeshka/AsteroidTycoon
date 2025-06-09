import math as m
import random as r
import drill as d
from tabulate import tabulate


class ScopeBreak(Exception):
    pass


class planet:
    planetMap = []
    drills: dict[str, d.drill] = {}
    x = 0
    y = 0

    def __init__(self, name):
        self.name = name
        self.planetMap = self.resourceScatter()
        self.drills = self.initializeDrillVacancy()
        self.lowTier = r.choice(["Iron", "Coal", "Copper", "Aluminum"])
        self.midTier = r.choice(["Gold", "Zinc", "Lithium"])
        self.highTier = r.choice(["Diamond", "Lead", "Plutonium"])
        self.userMap = self.generateSurface(13, 13, '???')

    def __str__(self):
        return self.name
    
    def generateSurface(self, x, y, fill):
        ret = []
        for i in range(0, y):
            ret.append([])
            for j in range(0, x):
                ret[i].append(fill)
        return ret

    def resourceScatter(self):
        #Generate base plane
        surface = self.generateSurface(13, 13, None)

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
                except IndexError:
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
                except IndexError:
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
    
    def initializeDrillVacancy(self):
        ret = {}
        for x in range(13):
            for y in range(13):
                ret[f'{x},{y}'] = None
        return ret

    def addDrill(self):
        self.userMap[self.y][self.x] += '\n(Drilling)'
        if self.drills[f'{self.x},{self.y}'] == None:
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
        tile = 100*self.planetMap[self.y][self.x]
        self.userMap[self.y][self.x] = f'{round(tile, 1)}%'
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
        return (1-t)*a + t*b
    
    def movePos(self):
        x_pos = -1
        y_pos = -1
        while x_pos > 0 or x_pos <= 14:
            try:
                x_pos = int(input("Please select an x position [1-13]: "))
            except:
                print("Please input an integer")
            if x_pos <= 0 or x_pos > 13:
                print("Please select a number from 1-13 (inclusive)")
            else:
                break
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
        self.x = self.y = 0
        print("Returning to station...")
        raise ScopeBreak
    
    def harvest(self, player):
        total = [0,0,0]
        for key in self.drills.keys():
            if self.drills[key] != None:
                produced = self.drills[key].mine(player) # Display total accumulated resources
                total[0] += produced[0]
                total[1] += produced[1]
                total[2] += produced[2]
        print('You produced:\n   '\
             + f'{self.lowTier}: {total[0]}\n   '\
             + f'{self.midTier}: {total[1]}\n   '\
             + f'{self.highTier}: {total[2]}')
        
    def displayMap(self):
        print(tabulate(self.userMap))
    
    planetOptions = { # Won't compile without this being at the bottom ¯\_(ツ)_/¯
        "Place Drill": addDrill,
        "Survey Ground": groundSurvey,
        "Move": movePos,
        "Show Map": displayMap,
        "Return to station and harves minerals": leavePlanet
    }