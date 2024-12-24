#Function accepts taxi driver route map for costumer. Function find minimum cost for taxi driver to reach home while picking costumers on road.Function using Bellman-Ford Algorithm.

def min_cost(WList, source, destination):
    infinity = 1+len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    distance,predecessor={},{}
    
    for u in WList.keys():
        distance[u]=infinity
        predecessor[u]=None
    
    distance[source]=0
    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                if distance[u]+d < distance[v]:
                    predecessor[v]=u
                    distance[v]=min(distance[v],distance[u]+d)
    
    path=[]
    step=destination
    while step != None:
        if step not in path:
            path.append(step)
            step=predecessor[step]
    return (distance[destination],path[::-1])

size = int(input())
edges = eval(input())
s = int(input())
d = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for directed graph
    WL[ed[0]].append((ed[1],ed[2]))
print(min_cost(WL,s,d))
