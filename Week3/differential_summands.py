#To find the maximum number of students who can be awarded with the given prize pool, so that no two children recieves the same prize

def optimal_summands(n):
    
    if n==1:
        return [1]
    
    dist = []
    
    for i in range(1, n):
    
        #Stopping at n/2 because we get repeating numbers after that
        if n > 2*i:
            dist.append(i)
            n = n - i
        
        else:
            dist.append(n)
            break
            
    return dist


n = int(input())

dist = optimal_summands(n)
print(len(dist))
print(*dist)
