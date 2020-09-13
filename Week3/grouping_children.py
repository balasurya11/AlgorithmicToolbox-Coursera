#To group children based on their age, so that the age of children in that group differs by atmost one!
#Using Grredy Method
def group(c):
    
    #Sort the age of childrem
    c.sort()
    n = len(c)
    
    #First step is to make a greedy move that is safe
    #So, we have the index i coinciding with leftmost age
    #We group the ages within the range of 1 from the first age
    val = c[0]
    i = 0
    ans = []
    
    while i < n:
        temp = []
        val = c[i]
        val += 1
        for item in c[i:]:
            if item <= val:
                temp.append(item)
                i = i + 1
            else:
                break
         
        ans.append(temp)
        #We, then reduced it to a subproblem

    return ans

c = list(map(int,input().split()))
print(group(c))
