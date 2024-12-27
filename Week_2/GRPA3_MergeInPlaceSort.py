#Merging Two List in place instead of using new list.

def mergeInPlace(A,B):
    n = len(A)
    m = len(B)
    
    for i in range(n):
        for j in range(m):
            if A[i] > B[j]:
                A.swap(i, B, j)
    for el in range(0,m):
        pos = el
        for j in range(el+1,m):
            if B[j] < B[pos]:
                pos = j
        B.swap(el, B, pos)
    return A, B
