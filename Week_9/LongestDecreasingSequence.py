#Function takes list of integers and returns longest decreasing sequence.

def LDS(L):
    n = len(L)
    # Initialize an array to store the length of LDS ending at each index
    dp = [1] * n
    # Array to reconstruct the LDS
    prev = [-1] * n

    # Fill the dp table
    for i in range(1, n):
        for j in range(i):
            if L[j] > L[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum value in dp (end of the LDS)
    max_length = max(dp)
    max_index = dp.index(max_length)

    # Reconstruct the LDS
    lds = []
    while max_index != -1:
        lds.append(L[max_index])
        max_index = prev[max_index]

    return lds[::-1]  # Reverse to get the correct order
