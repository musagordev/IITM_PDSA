# An internet service provider company wants to lay fiber to connect n cities labeled 0 to n-1.
# Find minimum cost spanning trees for fiberlinks. Function uses Prim's algorithm.

def FiberLink(WList):
    infinity = 1+len(WList.keys())*max([d for u in WList.keys() for v,d in WList[u]])
    visited, distance, TreeEdges, DistList = {},{},[],[]
    
    for u in WList.keys():
        visited[u],distance[u]=False,infinity
        
    visited[0]=True
    for v,d in WList[0]:
        distance[v]=d
    for i in WList.keys():
        mindist,nextv = infinity,None
        for u in WList.keys():
            for v,d in WList[u]:
                if visited[u] and (not visited[v]) and d < mindist:
                    mindist, nextv, nexte = d, v, (u,v)
        if nextv == None:
            break
        visited[nextv]=True
        TreeEdges.append(nexte)
        DistList.append(mindist)
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v]=min(distance[v],d)
    total=0
    for i in DistList:
        total=total+i
    return total
    
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))
