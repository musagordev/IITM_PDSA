# Create a private network to connect all camps around country. 
# Write a Python function connectCamps(AList, exCamp) that accepts the AList as described above and a camp exCamp, returns the minimum cost required to connect all the camps excluding the exCamp. 
# If the camps cannot be connected after excluding exCamp return -1. 
# The function will be called to check for the cost excluding each camp one by one so try to make it efficient that runs in O((m + n) log n), where m is the number of pairs of camps that can be connected.


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)
    
    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        if left_child_index < len(self.heap) and self.heap[left_child_index][0] < self.heap[smallest][0]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index][0] < self.heap[smallest][0]:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    
    def is_empty(self):
        return len(self.heap) == 0

def connectCamps(AList, exCamp):
    pq = MinHeap()
    visited = set()
    start_camp = next(iter(AList.keys() - {exCamp}))
    for neighbor, cost in AList[start_camp]:
        if neighbor != exCamp:
            pq.push((cost, start_camp, neighbor))
    visited.add(start_camp)
    total_cost = 0
    camps_connected = 1
    while not pq.is_empty() and camps_connected < len(AList) - 1:
        cost, u, v = pq.pop()
        if v not in visited:
            visited.add(v)
            total_cost += cost
            camps_connected += 1
            for neighbor, n_cost in AList[v]:
                if neighbor != exCamp and neighbor not in visited:
                    pq.push((n_cost, v, neighbor))
    if camps_connected == len(AList) - 1:
        return total_cost
    else:
        return -1
