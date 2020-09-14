def dot_product(a,b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]* b[i]
    return ans

n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
print(dot_product(a, b))
