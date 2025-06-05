from math import *
import random as r
import drill as d

class planet:
    planetMap = []
    drills = {}

    def __init__(self):
        self.planetMap = self.resourceScatter()
        self.drills = self.initializeDrillVacancy()
        self.lowTier = r.choice(["Iron", "Coal", "Copper", "Aluminium"])
        self.midTier = r.choice(["Gold", "Zinc", "Lithium"])
        self.highTier = r.choice(["Diamond", "Lead", "Plutonium"])

    def resourceScatter(self):
        #Generate base plane
        surface = [
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None,None,None,None,None,None]
        ]

        #Random height sample points
        for i in range(int(len(surface)/3)+1):
            for j in range(int(len(surface[i])/3)+1):
                surface[3*i][3*j] = r.random()

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
                        (i/3) - floor(i/3)
                    ) + self.lerp(
                        surface[i][3*round(j/3)],
                        surface[i][3*round(((j+3)/3)-0.5)],
                        (j/3) - floor(j/3)
                    ))/2
        return surface
    
    def initializeDrillVacancy(self):
        ret = {}
        for x in range(13):
            for y in range(13):
                ret[f'{x},{y}'] = None
        return ret

    def addDrill(self, x, y):
        if self.drills[f'{x},{y}'] == None:
            self.drills[f'{x},{y}'] = d.drill(self.planetMap[x][y],
                                               self.lowTier, self.midTier,
                                                 self.highTier)
        else:
            print("There is already a drill there!")

    def groundSurvey(self, x, y):
        tile = self.planetMap[x][y]
        if tile > 75:
            print(f'{100*tile}% Ore Concentration, very good!')
        elif tile > 50:
            print(f'{100*tile}% Ore Concentration, decent patch.')
        elif tile > 25:
            print(f'{100*tile}% Ore Concentration, less than ideal.')
        else:
            print(f'{100*tile}% Ore Concentration, rather awful.')

    def lerp(self, a, b, t):
        return (1-t)*a + t*b