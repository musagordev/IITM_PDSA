#In 2-D matrix, M[i][j] contains number of coins. Find a path to collect maximum coins between two points

import numpy as np
def MaxCoinPath(M,x1,y1,x2,y2):
    row = len(M)
    col = len(M[0])
    coin=np.zeros((row+1,col+1))
    
    coin[x1][y1] = M[x1][y1]
    
    for r in range(x1,x2+1):
        for c in range(y1,y2+1):
            if r == x1 and c == y1:
                continue
            top = coin[r-1][c]
            left = coin[r][c-1]
            coin[r][c] = M[r][c] + int(max(top,left))
    
    return int(coin[x2][y2])
