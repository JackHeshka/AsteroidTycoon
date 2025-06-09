from player.py import *
from math import round
import time as t

class drill:
    def __init__(self, oreAbundance, common, mid, rare):
        self.curr = t.time() #Time to add productivity
        self.productivity = oreAbundance
        self.common = common
        self.mid = mid
        self.rare = rare
    
    def mine(self, player):
        produced = int(t.time - self.curr)*self.productivity
        self.curr = t.time
        print('You produced:\n   '\
             + f'{self.common}: {round(0.7*produced)}\n   '\
             + f'{self.mid}: {round(0.25*produced)}\n   '\
             + f'{self.rare}: {round(0.05*produced)}')
        player.raw_inventory[self.common] += round(0.7*produced)
        player.raw_inventory[self.mid] += round(0.25*produced)
        player.raw_inventory[self.rare] += round(0.05*produced)