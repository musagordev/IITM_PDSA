Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive). 
The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.

def prime(a):
    pl=[]
    for i in range(1,a):
        if a % i == 0:
            pl.append(i)
    if len(pl) == 1:
        return True
    else: 
        return False

def Twin_Primes(a,b):
    tp = []
    for i in range(a,b+1):
        for j in range(i,b+1):
            if prime(i) and prime(j) and j-i == 2:
                tp.append((i,j))
    return(tp)
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
