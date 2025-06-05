import time as t

class drill:
    def __init__(self, oreAbundance, common, mid, rare):
        self.curr = t.time() #Time to add productivity
        self.productivity = oreAbundance
        self.common = common
    
    def mine(self):
        produced = int(t.time - self.curr)*self.productivity
        self.curr = t.time
        return produced