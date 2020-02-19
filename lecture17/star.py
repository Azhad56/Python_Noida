def starDown(stars):
    if stars==0:
        return
    for i in range(stars):
        print("*",end="")
    print()
    starDown(stars-1)

def starDownRec(row,col=0):
    if row==0:
        return
    if col == row:
        print()
        starDownRec(row-1,0)
        return
    print("*",end=" ")
    starDownRec(row,col+1)
starDown(5)
def starUp(stars):
    if stars==0:
        return
    starUp(stars-1)
    for i in range(stars):
        print("*",end="")
    print()



