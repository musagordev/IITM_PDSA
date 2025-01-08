#function shuffle(l1,l2) that takes two lists, l1 and l2 as input, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on.
#If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

def shuffle(l1,l2):
    m,n = len(l1), len(l2)
    L,i,j=[],0,0
    
    while i+j < m+n:
        if i == m:
            L.append(l2[j])
            j+=1
        elif j == n:
            L.append(l1[i])
            i+=1
        elif i == j:
            L.append(l1[i])
            i+=1
        elif i > j:
            L.append(l2[j])
            j+=1
    
    return L
            
    
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))
