class RulesSet():
    def __init__(self,r):
        self.rules = r
        self.values = []
        self.first = []
        self.follow = []
        self.buildValues()
        
    def buildValues(self):
        for i in self.rules:
            self.values.append(i[0][0:1])
        self.values = set(self.values)
        self.values = list(self.values) 
        for i in self.values:
            a = "holf"
    def First(self):
        for j in self.values:
            for i in self.rules:
                if i[0:1].isalpha()  == False:
                    b ="yo"
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
print(mainrules.values)