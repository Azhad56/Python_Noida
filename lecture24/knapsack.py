import numpy as np
def Knapsack(weights,prices,capacity,index=0):
    if (capacity==0) or (index==len(weights)):
        return 0
    left = 0
    if capacity >=weights[index]:
        left = prices[index] + Knapsack(weights,prices,capacity-weights[index],index+1)
    right = Knapsack(weights,prices,capacity,index+1)
    return max(left,right)
p = [7,8,6]
w = [10,15,5]
# print(Knapsack(w,p,20))

def KnapsackDp(weights,prices,capacity,memory,index=0):
    if (capacity==0) or (index==len(weights)):
        return 0
    if memory.get((capacity,index)):
        return memory.get((capacity,index))
    left = 0
    if capacity >=weights[index]:
        left = prices[index] + KnapsackDp(weights,prices,capacity-weights[index],memory,index+1)
    right = KnapsackDp(weights,prices,capacity,memory,index+1)
    res = max(left,right)
    memory[(capacity, index)] = res
    return res
p = list(np.random.randint(5,10,100))
w = list(np.random.randint(5,10,100))
print(KnapsackDp(w,p,20,{}))