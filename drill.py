import time as t

class drill:
    def __init__(self, oreAbundance):
        self.curr = t.time() #Time to add productivity
        self.productivity = oreAbundance
    
    def mine(self):
        produced = int(t.time - self.curr)*self.productivity
        self.curr = t.time
        return produced