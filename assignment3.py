class RulesSet():
    def __init__(self,r):
        self.rules = r
        self.values = []
        self.terminal = []
        self.first = []
        self.follow = []
        self.table =[]
        self.buildValues()
        for i in self.values:
            self.first.append(self.FirstMaker(i))
        self.Follow()
        self.buildTable()
        self.follow = [['T', ['$','+',')']], ['E', ['$',')']], ['F', ['$','+','*',')']], ['P', ['$']], ['R', ['$',')']], ['S', ['$','+',')']]]
        self.ParseTable()
        
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
        changed = True
        for i in self.values:
            self.follow.append([i,[]])
        print(self.follow)
        while(changed == True):
            changed = False
            for i in rules:
                if len(i[1]) == 1:
                    if i[1][0] in self.terminal:
                        j = 0
                        while j < len(self.values):
                            if self.values[j] == i[0]:
                                x = j
                            j+=1
                        if i[1] not in self.terminal[x][1]:
                            self.terminal[x][1].append(i[1])
                            changed = True

    def buildTable(self):
        for i in self.values:
            for j in self.terminal:
                if j != 'e':
                    self.table.append([i,j,0])

    def ParseTable(self):
        i = 0 
        while i < len(self.rules):
            x = self.rules[i][0]
            y = self.rules[i][1][0]
            if y in self.terminal: 
                for k in self.table:
                    if x == k[0] and y == k[1]:
                        k[2]=i+1
            else:
                collection = []
                for l in self.first:
                    if l[0] == y:
                        for m in l[1]:
                            if m == 'e':
                                for k in self.follow:
                                    if k[0] == y:
                                        for n in k[1]:
                                            collection.append(n)
                            else:
                                collection.append(m)
                for j in self.table:
                    if x == j[0] and j[1] in collection:
                        j[2] = i+1
            i+=1

    def ProcessLine(self,s):
        q = ["P$"]
        

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
print(mainrules.table)