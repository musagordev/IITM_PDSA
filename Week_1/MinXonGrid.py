#function Min_X(n, m) that accept the number of rows n and number of columns m as input and returns the minimum number of cells you need to put an X on in an n x m grid to achieve the desired result.

def Min_X(n,m):
    total_grid = m*n
    
    if total_grid % 3 == 0:
        minimum_x= total_grid//3
    else:
        minimum_x= 1+ total_grid//3
    
    return minimum_x
