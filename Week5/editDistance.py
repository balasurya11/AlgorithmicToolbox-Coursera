def compute_dist(a, b):
    
    x,y = len(a), len(b)
    
    dp = [[0 for i in range(y+1)] for j in range(x+1)]
    
    dp[0] = list(range(y+1))
    
    for i in range(x+1):
        dp[i][0] = i  
        
        
        
    for i in range(1, x+1):
        
        for j in range(1,y+1):
            
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            else:
                dp[i][j] = min(dp[i-1][j]+1, 
                              dp[i][j-1]+1,
                              dp[i-1][j-1]+1)

    return dp[x][y]

a = input()
b = input()

print(compute_dist(a, b))
