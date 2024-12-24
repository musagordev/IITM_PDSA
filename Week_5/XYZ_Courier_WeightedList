#A courier company XYZ provides courier service between n cities labeled 0 to n-1, where customers can send items from any city to any another city.
#Function accepts weighted adjacency list and return shortest route with minimum cost for destination from source.

class XYZ_Courier:
    def __init__(self,WList):
        self.WList = WList
        
    def cost(self,source,destination):
        WList = self.WList
        visited,distance =({},{})
        infinity=1+len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
        for u in WList.keys():
            visited[u], distance[u] = False, infinity
        
        distance[source]=0
        for u in WList.keys():
            nextd=min([distance[v] for v in WList.keys() if not visited[v]])
            nextvlist=[v for v in WList.keys() if not visited[v] and distance[v] == nextd]
            if nextvlist == []:
                break
            nextv = min(nextvlist)
            visited[nextv]=True
            for (v,d) in WList[nextv]:
                if not visited[v]:
                    distance[v] = min(distance[v],(distance[nextv]+d))
        return distance[destination] * 5 if distance[destination] != infinity else -1
    
    def route(self,source,destination):
        WList = self.WList
        visited,distance =({},{})
        predecessor = {}
        infinity=1+len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
        for u in WList.keys():
            visited[u], distance[u], predecessor[u] = False, infinity, None
        distance[source] = 0

        for i in WList.keys():
            nextd=min([distance[v] for v in WList.keys() if not visited[v]])
            nextvlist=[v for v in WList.keys() if not visited[v] and distance[v] == nextd]
            if nextvlist == []:
                break
            nextv = min(nextvlist)
            visited[nextv]=True
            for (v, d) in WList[nextv]:
                if not visited[v] and distance[nextv] + d < distance[v]:
                    distance[v] = distance[nextv] + d
                    predecessor[v] = nextv
        path = []
        step = destination
        while step is not None:
            path.append(step)
            step = predecessor[step]

        if path[-1] != source:
            return []
        return path[::-1]
        
    
size = int(input())
edges = eval(input())
s=int(input())
d=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
C = XYZ_Courier(WL)
print(C.cost(s,d))
print(C.route(s,d))
