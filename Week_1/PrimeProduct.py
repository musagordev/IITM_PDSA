#Check if a number is multiply of two prime number

def prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    factors=[]
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    if factors == [1,n]:
        return True
    else:
        return False

def prime_product(n):
    if n <= 1:
        return False
    prime_factors = []
    for i in range(n+1):
        for j in range(n+1):
            if prime(i) and prime(j) and i*j == n:
                prime_factors.append((i,j))
    if prime_factors:
        return True
    else:
        return False
n = int(input())
print(prime_product(n))
