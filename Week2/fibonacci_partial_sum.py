# Uses python3

def fibonacci_sum(n):
    n = n % 60
    
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10
        sum = sum%10 + current

    return sum % 10

def fibonacci_partial_sum(from_, to):
    

    return abs(fibonacci_sum(from_+2) - fibonacci_sum(to + 1))

from_, to = map(int, input().split())
print(fibonacci_partial_sum(from_, to))