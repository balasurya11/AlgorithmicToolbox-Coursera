def knapsack(capacity, weightList, valueList, valuePerWeight):

    maxValue = 0
    
    while capacity > 0 and weightList!= []:
        
        #Finding the max valuePerWeight and its indes
        maxValPerWeight = max(valuePerWeight)
        i = valuePerWeight.index(maxValPerWeight)
        
        #Take the minimum of, the quantity of the current item to fill the knapsack and the available capacity.
        taken = min(capacity, weightList[i])
        
        #Updating the maxValue
        maxValue += maxValPerWeight * taken
        
        #Updating the values for remaining subproblem
        capacity = capacity - taken
        del(valuePerWeight[i])
        del(weightList[i])
        
    return round(maxValue, 3)
        
noItems, capacity = map(int,input().split())

weightList = []
valueList = []
valuePerWeight = []

for _ in range(noItems):
    vl,wt = map(int,input().split())
    
    valueList.append(vl)
    weightList.append(wt)
    valuePerWeight.append(vl/wt)
    
print(knapsack(capacity, weightList, valueList, valuePerWeight))