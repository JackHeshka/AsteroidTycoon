from random import *

class planet:
    planetMap = []
    location = ''

    def __init__(self):
        pass

    def resourceScatter(self):
        #Generate base plane
        surface = [
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0]
        ]

        #Random height sample points
        for i in len(surface)/3:
            for j in len(surface[i])/3:
                surface[3*i][3*j] = random()

        #Linear interpolation
        #Vertical nodes
        for i in surface:
            segment = i/3
            for j in len(surface[i])/3:
                surface[i][3*j] = self.lerp(surface[3*int(segment)][3*j],
                                            surface[3*(int(segment)+1)][3*j],
                                            segment-int(segment))
        #Horizontal nodes
        for i in len(surface)/3:
            for j in surface[i]:
                surface[3*i][j] = self.lerp(surface[3*i][3*int(segment)],
                                            surface[3*i][3*(int(segment)+1)],
                                            segment-int(segment))
        #Average over the surface


    def lerp(self, a, b, t):
        return (1-t)*a + t*b