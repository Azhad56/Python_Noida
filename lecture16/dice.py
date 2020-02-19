def dice(processed,target,faces):
    if target == 0:
        print(processed)
        return
    for i in range(1,faces+1):
        if target <i:
            continue
        dice(processed+str(i),target-i,faces)
dice("",5,3)