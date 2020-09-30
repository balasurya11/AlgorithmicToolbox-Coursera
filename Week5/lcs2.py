l1 = int(input())
a = list(map(int,input().split()))
l2 = int(input())
b = list(map(int,input().split()))

#Memoized Version

mem = [[-1 for i in range(l1+1)] for j in range(l2+1)]

def lcs(a,b,m,n):

    if mem[n][m] != -1:
        return mem[n][m]
        
    if m==0 or n==0:
        mem[n][m] = 0
        return mem[n][m]
        
    elif a[m-1] == b[n-1]:
        mem[n][m]=1+lcs(a,b,m-1,n-1)
        return mem[n][m]
        
    mem[n][m] = max(lcs(a,b,m-1,n),lcs(a,b,m,n-1))
    
    return mem[n][m]

print(lcs(a,b,l1,l2))
