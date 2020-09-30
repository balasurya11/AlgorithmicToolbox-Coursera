def get_change(m):
    
    coins = [1,3,4]
    dp = [m+1] * (m+1)
    dp[0] = 0

    for i in range(1, m + 1):
    
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i-coin])
            else:
                break
    
    return dp[m]

m = int(input())
print(get_change(m))
