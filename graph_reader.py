class Graph:
    def __init__(self, file: str):
        self.adj = dict()
        self.Edges = list()
        self.Degrees = dict()
        self.W = 0
        self.L = 0 
        self.tauList = list()
        self.lambdaList = list()  
       # Read the file line by line. 
       # If the line is a comment, skip it. 
       # Otherwise, split the line into two integers, node1 and node2. 
       # If node1 is not in the adjacency list, add it to the adjacency list. 
       # If node2 is not in the adjacency list, add it to the adjacency list. 
       # If node2 is not in the adjacency list of node1, add it to the adjacency list of node1.
        with open(file) as reader:
            lines = reader.readlines()
            for i, line in enumerate(lines):
                if i%100000==0:
                    print(i)
                if line[0] == '#':
                    continue
                else:
                    node1, node2 = map(int, line.split())
                    if node1 not in self.adj:
                        self.adj[node1] = [node2]
                        self.Edges.append((node1, node2))
                    elif node2 not in self.adj[node1]:
                    #else:
                        self.adj[node1].append(node2)
                        self.Edges.append((node1, node2))

                    if node2 not in self.adj:
                        self.adj[node2] = [node1]
                    elif node1 not in self.adj[node2]:
                    #else:
                        self.adj[node2].append(node1) 
        # 1. For each node, sort the adjacency list by the degree of the nodes.
        # 2. Initialize the degrees dictionary.
        # 3. Initialize the w_lambda dictionary.
        for node in self.adj.keys():
            self.Degrees[node] = len(self.adj[node])
            nbrs = [(len(self.adj[u]), u) for u in self.adj[node]]
            _, nbrs = zip(*sorted(nbrs))
            self.adj[node] = list(nbrs) #sorted by (degree, index) adj list of node       
        self.count_w_lambda()

    def getDegree(self, node):
        '''
        Get the degree of a node.
        '''
        return self.Degrees[node]

  
    def isEdge(self, node1, node2):
        '''
        Given a node, return True if the node has an edge to another node. 
        '''
        if node2 in self.adj[node1]:    
            return True                     
        else: 
            return False
            
    def count_w_lambda(self):   
        '''
        For each edge (u,v) in the graph, calculate the number of triangles that include both u and v.

        '''
        for u, v in self.Edges:
            degree1 = self.getDegree(u)
            degree2 = self.getDegree(v)  
            tau = (degree1-1)*(degree2-1)
            self.W += tau
            self.tauList.append(tau)

            L_uv = degree1 - self.adj[u].index(v) - 1
            L_vu = degree2 - self.adj[v].index(u) - 1
            l = L_uv*L_vu
            self.lambdaList.append(l) 
            self.L += l