# python3
def compute_min_refills(distance, tank, stops):
    # write your code here
    n = len(stops)
    stops.insert(0,0)
    stops.append(distance)

    count, last_refill, current_refill = 0, 0, 0
    while current_refill <= n:
        last_refill = current_refill
        while current_refill<=n and stops[current_refill+1]-stops[last_refill]<=tank:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        
        if current_refill <= n:
            last_refill += 1
            count+=1
    return count



d = int(input())
m = int(input())
n = int(input())
stops = list(map(int,input().split()))
print(compute_min_refills(d, m, stops))
