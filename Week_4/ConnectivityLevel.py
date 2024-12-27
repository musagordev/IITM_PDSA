# Function finds a connection level between two vertices (Px, Py) in given graph matrices.

from collections import deque

def findConnectionLevel(n, Gmat, Px, Py):
    # If Px and Py are the same, connectivity level is 0 (same person)
    if Px == Py:
        return 0
    
    # Initialize a queue for BFS and a set to track visited nodes
    queue = deque([(Px, 1)])  # Start with Px and level 1
    visited = {v:False for v in range(n)}
    
    while queue:
        current_node, level = queue.popleft()
        
        # Explore all neighbors of the current node
        for neighbor in range(n):
            if Gmat[current_node][neighbor] == 1 and not visited[neighbor]:
                # If the neighbor is Py, return the current level + 1
                if neighbor == Py:
                    return level
                # Otherwise, add the neighbor to the queue with incremented level
                queue.append((neighbor, level + 1))
                visited[neighbor] = True
    
    # If we exit the loop without finding Py, return 0 (no connection)
    return 0

vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))
