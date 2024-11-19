class RulesSet():
    def __init__(self,r):
        self.rules = r
        self.values = []
        self.first = []
        self.follow = []
    
    def buildValues(self):
        for i in self.rules():
            self.values.append(i)
        for i in self.values():
            
    def First(self):
        for j in self.values():
            for i in self.rules():
                if i[0:1].isalpha()  == False:
               
    def Follow(self):
        self.follow = "woah"
    

file = open('grammar.txt','r')
rules = file.readlines()
points = []
for i in rules:
    entry = i.split()
    points.append(entry)
mainrules = RulesSet(points)
print(points)
