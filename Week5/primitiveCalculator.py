def optimal_sequence(n):

    dp = [n+1] * (n+1)
    dp[0] = -1
    dp[1] = 0

    for i in range(2,n+1):
        if i%2 == 0:
            dp[i] = min(dp[i], 1+dp[i//2])
        if i%3 == 0:
            dp[i] = min(dp[i], 1+dp[i//3])
        dp[i] = min(dp[i], 1+dp[i-1])

    i = n
    ans = [n]

    while i >= 2:

        if (i %3 == 0) and dp[i] == (dp[i//3]+1):
            ans.append(i//3)
            i = i//3
        elif (i %2 == 0) and dp[i] == (dp[i//2]+1):
            ans.append(i//2)
            i = i//2
        else:
            ans.append(i-1)
            i = i -1

    return reversed(ans)


n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
