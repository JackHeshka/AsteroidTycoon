from player import *
import time as t

class drill:
    def __init__(self, oreAbundance, ores):
        self.curr: float = t.time()
        self.productivity = oreAbundance
        self.common = ores['common']
        self.mid = ores['mid']
        self.rare = ores['rare']
    
    def mine(self, player):
        '''
        This function will calculate how much ore was produced by the drill
        based on time passed, and concentration at its location.
        It then adds the resources to the players inventory and returns
        a log of what was produced
        '''
        # Calculate time passed, in seconds, and multiply by productivity
        produced = int(t.time() - self.curr)*self.productivity
        self.curr = t.time()
        # Add resources to player inventory
        player.raw_inventory[self.common] += round(0.7*produced)
        player.raw_inventory[self.mid] += round(0.25*produced)
        player.raw_inventory[self.rare] += round(0.05*produced)
        return [round(0.7*produced),
                 round(0.25*produced),
                 round(0.05*produced)]