# Create Min Heap class and insert, delete elements from it.
# Create a function to if argument number is greated-r than k'th smallest element in the min heap.

class Min_Heap:
    def __init__(self):
        self.A=[]
    
    def heapify_up(self, index):
        parent=(index-1)//2
        if index > 0 and self.A[index] < self.A[parent]:
            self.A[index], self.A[parent] = self.A[parent], self.A[index]
            self.heapify_up(parent)
    
    def insert(self, el):
        self.A.append(el)
        self.heapify_up(len(self.A) - 1)
        
    def delete_min(self):
        if len(self.A) > 1:
            min_val = self.A[0]
            self.A.pop()
            self.heapify_up(len(self.A) - 1)
        elif self.A:
            min_val = self.A.pop()
        else:
            min_val = None
        return min_val

def KminGreaterThan(arr,k,num):
    heap=Min_Heap()
    for i in arr:
        heap.insert(i)

    final_num=heap.A[k-1]

    if final_num >= num:
        return True
    else:
        return False
        
