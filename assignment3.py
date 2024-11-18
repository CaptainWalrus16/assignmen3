file = open('grammar.txt','r')
rules = file.readlines()
points = []
for i in rules:
    entry = i.split()
    points.append(entry)
mainrules = RulesSet(points)

class RulesSet():
    def __init__(self,r):
        self.rules = r
        self.first
        self.follow
    
    def First(self):
        
    def Follow(self):
        