#Function takes list L, check if every pair of element's absolute difference increasing.

def expanding(L):
    diff = -1
    n= len(L)
    for i in range(1,n):
        if abs(L[i] - L[i-1]) > diff:
            diff = abs(L[i] - L[i-1])
        else:
            return False
    return True
            
L = eval(input())
print(expanding(L))
