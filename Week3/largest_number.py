def isBetter(a, b):

    #Function to check either the sequence 'ab' or 'ba' is better. If a is better, returns True else False
    a, b = str(a), str(b)
    n1 = int(a+b)
    n2 = int(b+a)
    
    if n2 > n1:
        return True
    return False
            
def largest_number(a):

    #Empty list to store the answer
    number = []
    
    while a != []:
        maxDigit = a[0]
        
        #Loop to find the best digit to have in the front from the list a
        for i in range(1, len(a)):
            if isBetter(maxDigit, a[i]):
                maxDigit = a[i]
                
        number.append(maxDigit)
        
        #Remove the item added to the answer list
        #Reduced it to a subproblem and repeat the process until there are no more subproblems left
        a.remove(maxDigit)
        
    return number

n = int(input())
l = list(map(int,input().split()))
l = largest_number(l)
ans = ''
for item in l:
    ans += str(item)
print(int(ans))
    
