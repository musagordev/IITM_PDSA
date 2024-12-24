# Create Min Heap to use in sorting
# Write a function to merge all list into a single list. With time complexity O(nlogn)

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

def mergeKLists(L):
    min_heap = MinHeap()
    result = []
    
    for i in range(len(L)):
        if L[i]:  
            min_heap.push((L[i][0], i, 0))  
    

    while not min_heap.is_empty():
        val, list_idx, elem_idx = min_heap.pop()
        result.append(val)
        
        if elem_idx + 1 < len(L[list_idx]):
            next_val = L[list_idx][elem_idx + 1]
            min_heap.push((next_val, list_idx, elem_idx + 1))
    
    return result

k = int(input())
LL=[]
for i in range(k):
    subL = [int(item) for item in input().split(" ")]
    LL.append(subL)
print(*mergeKLists(LL))
