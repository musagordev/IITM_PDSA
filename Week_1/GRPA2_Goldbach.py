def prime(a):
    pl=[]
    for i in range(1,a):
        if a % i == 0:
            pl.append(i)
    if len(pl) == 1:
        return True
    else: 
        return False
        
def Goldbach(n):
    L=[]
    for i in range(n):
        for j in range(i,n):
            if prime(i) and prime(j):
                if i + j == n:
                    L.append((i,j))
    return L
    
n=int(input())
print(sorted(Goldbach(n)))
