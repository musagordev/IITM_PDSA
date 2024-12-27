# In a given maze (X represents to wall, ' ' represents allowed tiles, '*' represents target) 
# Python function to find if target is reachable in maze with BreadDepthFirst search method.

def preprocessing(maze):
    m, n = len(maze), len(maze[0])
    S, E, K = None, None, None
    AList = {}
    allowedTiles = [' ', '*']

    # Create adjacency list and identify S, E, and K
    for i in range(m):
        for j in range(n):
            AList[(i, j)] = []
            if maze[i][j] in allowedTiles:
                # Check all four directions (down, up, right, left)
                if i + 1 < m and maze[i + 1][j] in allowedTiles:
                    AList[(i, j)].append((i + 1, j))
                if i - 1 >= 0 and maze[i - 1][j] in allowedTiles:
                    AList[(i, j)].append((i - 1, j))
                if j + 1 < n and maze[i][j + 1] in allowedTiles:
                    AList[(i, j)].append((i, j + 1))
                if j - 1 >= 0 and maze[i][j - 1] in allowedTiles:
                    AList[(i, j)].append((i, j - 1))

            # Identify start (S), end (E), and special point (K)
            if j == 0 and maze[i][j] == ' ':
                S = (i, j)
            if j == n - 1 and maze[i][j] == ' ':
                E = (i, j)
            if maze[i][j] == '*':
                K = (i, j)

    return AList, S, E, K

def BFS(AList, start):
    visited = {k: False for k in AList.keys()}
    level = {k: None for k in AList.keys()}
    queue = []

    visited[start] = True
    level[start] = 0
    queue.append(start)

    while queue:
        v = queue.pop(0)
        for neighbor in AList[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                if level[neighbor] is None:
                    level[neighbor] = level[v] + 1

    return level

# Input and processing
maze = []
line = input()
while line:
    maze.append(line)
    line = input()

AList, S, E, K = preprocessing(maze)
level = BFS(AList, S)

# Check for reachability from S to K
if level[K] is None:
    print(-1)
else:
    # Check for reachability from K to E
    level2 = BFS(AList, K)
    if level2[E] is None:
        print(-2)
    else:
        # Print the total distance
        print(level[K] + level2[E])
