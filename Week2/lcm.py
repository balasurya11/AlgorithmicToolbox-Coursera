# Uses python3
def gcd(a, b):

    while b!=0:
        a,b = b,a%b

    return a

a, b = map(int, input().split())
lcm = a*b/gcd(a, b)
print(int(lcm))