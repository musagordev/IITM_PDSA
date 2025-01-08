# Problem: Maximum Amount of Money

#Ram has a list of integers `a1, a2, ..., an` of size `n`. Each integer at index `i` denotes the money placed at that index `i`. He can do the following operation **exactly once**:

#- Pick a subsegment of the list and cyclically rotate it in the clockwise direction by any amount.  
#  i.e., pick integers `l` and `r` such that `1 ≤ l ≤ r ≤ n`, and rotate the list `a[l], a[l+1], ..., a[r]` in the clockwise direction by any amount.

#Ram wants the maximum amount of money by performing this particular operation exactly once. After performing the operation, Ram will collect `a[n] - a[1]` amount of money.

## Task

#Determine the **maximum value** of `a[n] - a[1]` that he can obtain.

#Write a function `Max_Amount(a)` that accepts a list `a` and returns the maximum value of `a[n] - a[1]` that Ram can obtain.

---

def Max_Amount(a):
    n = len(a)
    max_difference = float('-inf')

    # Iterate over all possible subsegments [l, r]
    for l in range(n):
        for r in range(l, n):
            # Rotate the subsegment [l, r]
            subsegment = a[l:r+1]
            for i in range(len(subsegment)):
                rotated = subsegment[i:] + subsegment[:i]
                new_array = a[:l] + rotated + a[r+1:]
                max_difference = max(max_difference, new_array[-1] - new_array[0])

    return max_difference

