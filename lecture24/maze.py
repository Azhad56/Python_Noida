def maze(row,col):
    if row == 0 and col ==0:
        return 1
    acc=0
    if row >0:
        acc +=maze(row-1,col)
    if col >0:
        acc +=maze(row,col-1)
    return acc
# print(maze(5,4))

def mazedp(row,col,memory):
    if row == 0 and col ==0:
        return 1
    if memory.get((row,col)):
        return memory.get((row,col))
    acc=0
    if row >0:
        acc +=mazedp(row-1,col,memory)
    if col >0:
        acc +=mazedp(row,col-1,memory)
    memory[(row,col)] = acc
    return acc
print(mazedp(5,4,{}))