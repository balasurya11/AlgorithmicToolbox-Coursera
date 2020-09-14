#Given the arrival time and exit time of each tenants, collect signatures from tenants with minimum possible visits
#Get the array and sort them according to their exit times
#Take the first exit time and compare it with the entry time of the others.
#If they've entered before the initial exit, continue
#Else, append the exit time of the first person and continue the same procedure for the subproblem

def covering_segments(l, n):
    i = 0
    coordinates = []
    
    while i<n:
        current = l[i]
        while i < n-1 and current[1] >= l[i+1][0]:
            i = i + 1
        coordinates.append(current[1])
        i = i + 1
        
    return coordinates
                
n = int(input())
l = []
for _ in range(n):
    temp = list(map(int,input().split()))
    l.append(temp)
l.sort(key = lambda x: x[1])

coordinates = covering_segments(l,n)
print(len(coordinates))
print(*coordinates)
    
