#Python function takes a list. Check sums of even and odd numbers seperately. And returns list with 2 element. 1st element is square of odd numbers, 2nd element is square of even numbers.

def odd(x):
    if x % 2 != 0:
        return True
    return False
    
def even(x):
    if x % 2 == 0:
        return True
    return False

def sumsquare(L):
    odd_l = 0
    even_l = 0
    for el in L:
        if odd(el):
            sqr = el ** 2
            odd_l += sqr
        elif even(el):
            sqr = el ** 2
            even_l += sqr
    
    final_L = [odd_l,even_l]
    return final_L
            
L = eval(input())
print(sumsquare(L))
