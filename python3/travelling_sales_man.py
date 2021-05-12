from sys import maxsize
from itertools import permutations

def tsp(graph,s):
    v=len(graph)
    vertices=[]
    for x in range(v):
        if x!=s:
            vertices.append(x)
    minpath=maxsize
    perm=permutations(vertices)
    
    for i in perm:
        current=0
        k=s
        for j in i:
            current+=graph[k][j]
            k=j
            
        current+=graph[k][s]
        minpath=min(minpath,current)
    return minpath
        
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
tsp(graph,s)

# time complexity for tsp O((n^2) * (2^n))
    
