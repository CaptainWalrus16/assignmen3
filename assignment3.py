class RulesSet():
    def __init__(self,r):
        self.rules = r
        self.values = []
        self.terminal = []
        self.first = []
        self.follow = []
        self.buildValues()
        for i in self.values:
            self.first.append(self.FirstMaker(i))
       
        
    def buildValues(self):
        for i in self.rules:
            self.values.append(i[0][0:1])
        self.values = set(self.values)
        self.values = list(self.values) 
        for i in self.rules:
            for j in i[1]:
                if j not in self.values:
                    self.terminal.append(j)
        self.terminal = set(self.terminal)
        self.terminal = list(self.terminal)
    
    def FirstMaker(self,i):
        self.filler=[]
        self.First(i)
        self.filler = set(self.filler)
        self.filler = list(self.filler)
        return [i,self.filler]
        
        
    def First(self,v):
        for i in self.rules:
            if v == i[0]:
                if i[1][0] in self.values:
                    self.First(i[1][0])
                else:
                    self.filler.append(i[1][0])
        
                                
    def Follow(self):
        
        
    

file = open('grammar.txt','r')
rules = file.readlines()
points = []
for i in rules:
    entry = i.split()
    points.append(entry)
mainrules = RulesSet(points)
print(points)
print(mainrules.values)
print(mainrules.terminal)
print(mainrules.first)