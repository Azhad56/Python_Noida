# def power(x,p):
#     if p==0:
#         return 1
#     return x * power(x,p-1)
# print(power(2,4))

# def fibo(n):
#     if n<2:
#         return n
#     first = fibo(n-1)
#     second = fibo(n-2)
#     return first + second
# print(fibo(5))

# def subseq(processed,unprocessed):
#     if len(unprocessed) ==0:
#         print(processed)
#         return
#     ch = unprocessed[0]
#     subseq(processed+ch,unprocessed[1:])
#     subseq(processed,unprocessed[1:])
# subseq("","abc")

# from itertools import permutations
# def allPermutations(str):
#     permList = permutations(str)
#     for perm in list(permList):
#         print(''.join(perm))
# allPermutations("abc")

def permute(processed,unprocessed):
    if len(unprocessed) ==0:
        print(processed)
        return
    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec_unprocessed = unprocessed[:i] + unprocessed[i+1:]
        permute(processed+ch,rec_unprocessed)
permute("","abc")

def maze(processed,row,col):
    if (row == 1) and (col == 1):
        print(processed)
        return
    if col >0:
        maze(processed + "H",row,col-1)
    if row >0:
        maze(processed + "V",row-1,col)
maze("",2,2)

# def mazeWD(processed,row,col):
#     if (row == 1) and (col == 1):
#         print(processed)
#         return
#     if col >0:
#         mazeWD(processed + "H",row,col-1)
#     if row >0:
#         mazeWD(processed + "V",row-1,col)
#     if (row >0) and (col >0):
#         mazeWD(processed+"D",row-1,col-1)
# mazeWD("",2,2)