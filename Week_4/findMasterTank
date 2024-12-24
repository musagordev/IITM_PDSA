#In a system of n water tanks on a hill, connected via m pipes. Water can flow through only one direction
#From source pipe find a master tank. Master tank is a tank that all the tanks in this group can be filled by connecting the water source to this master rank.

def findMasterTank(tanks, pipes):
    n = len(tanks)
    # Create an adjacency list and track the in-degrees of each tank
    adj_list = {tank: [] for tank in tanks}
    in_degree = {tank: 0 for tank in tanks}
    
    # Build the graph from the pipes and update in-degrees
    for (i, j) in pipes:
        adj_list[i].append(j)
        in_degree[j] += 1

    # Identify potential master tanks (tanks with zero in-degree)
    potential_masters = [tank for tank in tanks if in_degree[tank] == 0]

    if len(potential_masters) != 1:
        return 0
    
    # There should be only one potential master; we need to confirm it reaches all other nodes
    master = potential_masters[0]
    visited = set()

    def dfs(tank):
        visited.add(tank)
        for neighbor in adj_list[tank]:
            if neighbor not in visited:
                dfs(neighbor)

    # Perform DFS starting from the potential master
    dfs(master)

    # Check if all tanks are reachable from the master
    if len(visited) == n:
        return master
    else:
        return 0
v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))
