#Python function kthLargest(arr, k) that accepts a list arr of integers of size n and an integer k, such that k < = n and returns the kth largest integer in arr. The solution should run in O(n) time.

def quickselect(L,l,r,k):
  if (k < 1) or (k > r-l):
    return(None)

  (pivot,lower,upper) = (L[l],l+1,l+1)
  for i in range(l+1,r):
    if L[i] < pivot:  #
      upper = upper + 1
    else: 
      (L[i], L[lower]) = (L[lower], L[i])
      (lower,upper) = (lower+1,upper+1)
  (L[l],L[lower-1]) = (L[lower-1],L[l]) 
  lower = lower - 1

  lowerlen = lower - l
  if k <= lowerlen:
    return(quickselect(L,l,lower,k))
  elif k == (lowerlen + 1):
    return(L[lower])
  else:
    return(quickselect(L,lower+1,r,k-(lowerlen+1)))

def kthLargest(arr,k):
    sorted_arr = quickselect(arr,0,len(arr),k)
    return sorted_arr
arr=[int(item) for item in input().split(" ")]
k=int(input())
print(kthLargest(arr, k))
