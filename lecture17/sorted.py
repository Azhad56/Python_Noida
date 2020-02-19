def is_sorted(li,index=0):
    if index == (len(li) -1):
        return True
    current = li[index] <= li[index+1]
    remaining = is_sorted(li,index+1)
    return current and remaining
print(is_sorted([11,12,1,13]))

def contains(li,target,index=0):
    if index==len(li):
        return False
    current = li[index]==target
    remaining = contains(li,target,index+1)
    return current or remaining
# print(contains([11,12,13],12))