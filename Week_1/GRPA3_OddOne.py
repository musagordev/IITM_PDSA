#In the list L, all element types are same except one. Functions return types of elements in L

def odd_one(L):
    el_type = None
    if type(L[0])==type(L[1]) or type(L[0])==type(L[2]):
        el_type = type(L[0])
    elif type(L[0])==type(L[1]) or type(L[1])==type(L[2]):
        el_type = type(L[1])
    diff_type=None
    for el in L:
        if type(el) != el_type:
            diff_type = type(el)
    if diff_type == float:
        return('float')
    elif diff_type == int:
        return('int')
    elif diff_type == bool:
        return('bool')
    elif diff_type == str:
        return('str')
            
print(odd_one(eval(input().strip())))
