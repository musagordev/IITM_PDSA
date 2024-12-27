# Function checks if graph has negative weighted cycles

def IsNegativeWeightCyclePresent(WList):
    # Number of vertices
    num_vertices = len(WList)
    
    # Initialize distances with infinity, and set source distance to 0
    distances = {node: float('inf') for node in WList}
    source = next(iter(WList))  # Select any node as the source
    distances[source] = 0

    # Perform |V| - 1 iterations of relaxing all edges
    for _ in range(num_vertices - 1):
        for u in WList:
            for v, weight in WList[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # Check for negative weight cycles by trying one more relaxation
    for u in WList:
        for v, weight in WList[u]:
            if distances[u] + weight < distances[v]:
                # If we can relax further, then a negative cycle exists
                return True

    # If no negative weight cycle was found
    return False

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))
