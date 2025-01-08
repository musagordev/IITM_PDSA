# Function takes a list of integers, for each number of n occurs r times, function will return list of (n,r) tuples.

def histogram(l):
    l_dict ={}
    
    for i in l:
        if i not in l_dict:
            l_dict[i] = 1
        else:
            l_dict[i] += 1
    
    sorted_dict = dict(sorted(l_dict.items(), key=lambda item: (item[1], item[0])))
    
    final_L=[]
    for k,v in sorted_dict.items():
        final_L.append((k,v))
    
    return final_L
    
L=eval(input())
print(histogram(L))
