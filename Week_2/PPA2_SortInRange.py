#Sorting list with O(n+r) time complexity where n is lenght of list L, where list has integers which in range of 0 <= i < r.

def sortInRange(L,r):
  d={}
  for i in L:
    if i not in d:
      d[i]=1
    else:
      d[i]+=1
  T=[]
  for j in range(r):
    if j in d:
      T.extend([j]*d[j])
  L[:]=T
  return L
