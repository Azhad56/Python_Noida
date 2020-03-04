def dice(target,faces):
    if target ==0:
        return 1
    acc = 0
    for face in range(1,faces+1):
        if face >target:
            continue
        acc += dice(target-face,faces)
    return acc
print(dice(3,2))
def diceDp(target,faces,memory):
    if target == 0:
        return 1
    if memory.get(target):
        return memory.get(target)
    acc = 0
    for face in range(1,faces+1):
        if face > target:
            continue
        acc += diceDp(target-face,faces,memory)

    memory[target] = acc
    return acc
# print(diceDp(3,2,{}))