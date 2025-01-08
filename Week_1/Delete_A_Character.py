#Function take string (s), delete a character (c)
#If given parameter c is longer than 1 character, function will not work.

def del_char(s,c):
    if len(c) != 1:
        return s
    str=[]
    for el in s:
        if el != c:
            str.append(el)
    new_str = "".join(str)
    return(new_str)
s = input()
c = input()
print(del_char(s,c))
