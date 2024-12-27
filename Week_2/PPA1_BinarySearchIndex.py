#It is a function that accepts list L, integer k and integer a. It will search integer k in the List L with binarysearch method. It will return True if k in list, otherwise it will return False. It will also return how many times number compared.

def binarySearchIndexAndComparisons(L,k,a=0):
    if L == []:
        return (False, a)
    
    n = (len(L)-1)//2
    if L[n] == k:
        a+=1
        return (True, a)
    
    if k < L[n]:
        a+=1
        return binarySearchIndexAndComparisons(L[:n],k,a)
    else:
        a+=1
        return binarySearchIndexAndComparisons(L[n+1:],k,a)
        
