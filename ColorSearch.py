

class MapColor:
    
    def check_valid(self, graph):
        for node,nexts in graph.items():
            assert(nexts) # no isolated node
            assert(node not in nexts) # # no node linked to itself
            for nextNeighbor in nexts:
                assert(nextNeighbor in graph and node in graph[nextNeighbor]) # A linked to B implies B linked to A
        self.recursiveCalls = 0

    def __init__(self, graph, colors):
        self.check_valid(graph) #makes sure the graph is a real graph
        self.graph = graph
        nodes = list(self.graph.keys()) #keys are viewed as nodes
        self.node_colors  = { node: None for node in nodes } #making a dict of colors
        self.domains = { node: set(colors) for node in nodes } #making a dict for the domains


    def solveMostConstrainingVariable(self): #Most constraining variable search
        self.recursiveCalls = self.recursiveCalls + 1
        uncoloredNodes = [n for n,c in self.node_colors.items() if c is None] #getting all the uncolored nodes and put them in a list
        if not uncoloredNodes: #if the node has color
            print(self.node_colors)
            print(self.recursiveCalls - 1)
            return True

        node = self.mostConstrainingVariable(uncoloredNodes) #make the node all of the uncolored nodes
        for color in self.domains[node].copy():
            if all(color != self.node_colors[n] for n in self.graph[node]): #make sure our graph lines up with out node
                self.set_color(node, color) #changes the color of the uncolored node
                self.remove_from_domains(node, color) #take out the node from the domain
                
                if(self.solveMostConstrainingVariable()):
                    return True
    
                self.set_color(node, None) #make the color node
                self.add_to_domains(node, color) #add the node to the domain

        return False
    
    def solveMCV(self): 
        self.recursiveCalls = self.recursiveCalls + 1
        uncoloredNodes = [n for n,c in self.node_colors.items() if c is None]
        if not uncoloredNodes:
            print(self.node_colors)
            print(self.recursiveCalls - 1)
            return True

        node = self.MCV(uncoloredNodes) 
        for color in self.domains[node].copy():
            if all(color != self.node_colors[n] for n in self.graph[node]):
                self.set_color(node, color)
                self.remove_from_domains(node, color)
                
                if self.solveMCV():
                    return True
    
                self.set_color(node, None)
                self.add_to_domains(node, color)

        return False
    
    def solveLCV(self): 
        self.recursiveCalls = self.recursiveCalls + 1
        uncoloredNodes = [n for n,c in self.node_colors.items() if c is None]
        if not uncoloredNodes:
            print(self.node_colors)
            print(self.recursiveCalls - 1)
            return True

        node = uncoloredNodes[0]
        print('domain for '  + node + ': ' + str(self.domains[node]))
        bestColor = self.LCV(node, uncoloredNodes)
        if(bestColor == False):
            print(self.recursiveCalls)
            print("No solution.")
            return False
        if (bestColor != self.node_colors[n] for n in self.graph[node] and bestColor):
            self.set_color(node, bestColor)
            self.remove_from_domains(node, bestColor)
                
            if(self.solveLCV()):
                return True
    
            self.set_color(node, None)
            self.add_to_domains(node, bestColor)

        return False

    
    
    def MCV(self, uncoloredNodes):
        mostLikelyToFail = 99999999
        returnNode = 50
        for i in range(len(uncoloredNodes)):
            node = uncoloredNodes[i]
            if(len(self.domains[node]) < mostLikelyToFail):
                returnNode = node
                mostLikelyToFail = len(self.domains[node])
        return returnNode
    
    def mostConstrainingVariable(self, uncoloredNodes):
        mostConstraints = -5000
        returnNode = 50
        for i in range(len(self.graph)):
            while(i >= len(uncoloredNodes)):
                i = i - 1
            node = uncoloredNodes[i]
            if(len(self.graph[node]) > mostConstraints):
                returnNode = node
                mostConstraints = len(self.graph[node])
        return returnNode
    
    def LCV(self, node, uncoloredNodes):
        blue = 0
        red = 0
        green = 0
        if(self.domains[node] == set()):
            return False
        for color in self.domains[node]:
            for places in self.graph[node]:
                if(color in self.domains[places] and color == 'b'):
                    blue = blue + 1
                if('r' not in self.domains[node]):
                    red = red + 10000000000
                if(color in self.domains[places] and color == 'g'):
                    green = green + 1
                if('g' not in self.domains[node]):
                    green = green + 10000000000
                if(color in self.domains[places] and color == 'r'):
                    red = red + 1
                if('b' not in self.domains[node]):
                    blue = blue + 10000000000      
                    
        minimum = min((red, 'r'), (blue, 'b'), (green, 'g'))
    
        return minimum[1]
        

            
    
    def set_color(self, key, color):
        self.node_colors[key] = color
        

    def remove_from_domains(self, key, color):
        for node in self.graph[key]:
            if color in self.domains[node]:
                self.domains[node].remove(color)

    def add_to_domains(self, key, color):
        for node in self.graph[key]:
            self.domains[node].add(color)



WA  = 'western australia'
NT  = 'northwest territories'
SA  = 'southern australia'
Q   = 'queensland'
NSW = 'new south wales'
V   = 'victoria'
T   = 'tasmania'

colors    = {'r', 'g', 'b'}

australia = { T:   {V                },
              WA:  {NT, SA           },
              NT:  {WA, Q, SA        },
              SA:  {WA, NT, Q, NSW, V},
              Q:   {NT, SA, NSW      },
              NSW: {Q, SA, V         },
              V:   {SA, NSW, T       } }

problem = MapColor(australia, colors)

problem.solveLCV()