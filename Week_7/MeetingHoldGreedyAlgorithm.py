#A popular meeting hall in a city receives many overlapping applications to hold meetings.
#The manager wishes to satisfy as many customers as possible.
#Each application is a tuple (id, start_day, end_day) where id, start_day, 
#and end_day are the unique id assigned to the application, starting day of the meeting, and ending day of the meeting (inclusive), respectively.

def tuplesort(L, index):
    L_ = []
    for t in L:
        L_.append(t[index:index+1] + t[:index] + t[index+1:])
    L_.sort()

    L__ = []
    for t in L_:
        L__.append(t[1:index+1] + t[0:1] + t[index+1:])
    return L__

def no_overlap(L):
    sortedL = tuplesort(L, 2)
    accepted = [sortedL[0][0]]
    for i, s, f in sortedL[1:]:
        if s > L[accepted[-1]][2]:
            accepted.append(i)
    return accepted
