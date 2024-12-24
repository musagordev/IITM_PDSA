#Function takes a list of unique strings as an argument. It returns two list. 
#First list returns, list sorted in ascending order with respect to first character only.
#Second list returns, additional to the first list, it sort the remaining characters of string in descending order with respect to remaining characters.

def combinationSort(strList):
    L_c = strList.copy()
    
    n = len(strList)
    for i in range(n):
        j = i
        while(j > 0 and strList[j][0] < strList[j-1][0]):
            (strList[j],strList[j-1]) = (strList[j-1],strList[j])
            j = j-1
    
    for i in range(n):
        pos = i
        npos = i
        for j in range(i+1,n):
            if L_c[j][0] < L_c[pos][0]:
                pos=j
        L_c[i], L_c[pos] = L_c[pos], L_c[i]
        for j in range(i+1,n):
            if L_c[j][0] == L_c[npos][0]:
                if int(L_c[j][1:]) > int(L_c[npos][1:]):
                    npos = j
        L_c[npos], L_c[i] = L_c[i], L_c[npos]
    
    return strList, L_c

    
        
