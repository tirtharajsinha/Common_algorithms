class mst:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[]
        
    def addedge(self,s,d,w):
        self.graph.append([s,d,w])
        
    def findparent(self,parent,i):
        if parent[i]==i:
            return i
        return self.findparent(parent,parent[i])
    
    def union(self,parent,rank,x,y):
        xp=self.findparent(parent,x)
        yp=self.findparent(parent,y)
        
        if rank[xp]<rank[yp]:
            parent[xp]=yp
        elif rank[xp]>rank[yp]:
            parent[yp]=xp
        else:
            parent[yp]=xp
            rank[xp]+=1
    
    def kruskal(self):
        result=[]
        parent=[]
        rank=[]
        
        self.graph = sorted(self.graph, key=lambda x:x[2])
        for j in range(self.vertices):
            parent.append(j)
            rank.append(0)
            
        i,e=0,0
        
        while e<self.vertices-1:
            
            s,d,w=self.graph[i]
            i+=1
            
            x=self.findparent(parent,s)
            y=self.findparent(parent,d)
            
            if x!=y:
                e+=1
                result.append([s,d,w])
                self.union(parent,rank,x,y)
        self.display(result)
        
    def display(self,result):
        cost=0
        for edge in result:
            print(edge[0],"-->",edge[1],":",edge[2])
            cost+=edge[2]
        print("cost of minimal spanning tree = ",cost)
    
g = mst(6)
g.addedge(0, 1, 4)
g.addedge(0, 2, 4)
g.addedge(1, 2, 2)
g.addedge(1, 0, 4)
g.addedge(2, 0, 4)
g.addedge(2, 1, 2)
g.addedge(2, 3, 3)
g.addedge(2, 5, 2)
g.addedge(2, 4, 4)
g.addedge(3, 2, 3)
g.addedge(3, 4, 3)
g.addedge(4, 2, 4)
g.addedge(4, 3, 3)
g.addedge(5, 2, 2)
g.addedge(5, 4, 3)

g.kruskal()

# time complexity is O(ElogE) or O(ElogV)
