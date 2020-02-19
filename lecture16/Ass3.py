def printrow(num):
    if num==0:
        return
    print("*",end=" ")
    printrow(num-1)
def printpattern(n,i):
    if n==0:
        return
    printrow(i)
    print("\n","")
    printpattern(n-1,i-1)
printpattern(5,5)