# Function finds minimum cost to walk from source to destination with walking through another vertices. 
# min_cost function finds shortest path with minimum cost between two vertices
# min_cost_walk function find shortest path with minimum cost between two vertices with walking through another vertices V

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

def min_cost_walk(WList, S, D, V):
    # First, find the minimum cost and path from S to V
    cost_S_to_V, path_S_to_V = min_cost(WList,S,V)
    
    # Then, find the minimum cost and path from V to D
    cost_V_to_D, path_V_to_D = min_cost(WList,V,D)
    
    # Combine the paths and costs
    if path_S_to_V[-1] == V:
        full_path = path_S_to_V + path_V_to_D[1:]  # Avoid repeating V in the path
    else:
        full_path = path_S_to_V + path_V_to_D
    
    total_cost = cost_S_to_V + cost_V_to_D
    
    return total_cost, full_path

size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))
