#Find the largest number in the List, which is ascending order and rotated n times. O(logn) times complexity.

def findLargest(L):
    left, right = 0, len(L) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than the rightmost element, the pivot (max element) is on the right
        if L[mid] > L[right]:
            left = mid + 1
        else:
            right = mid
            
    # When the loop ends, left == right and it points to the largest element
    return L[left - 1]  # Adjusting for the last step where left crosses over
