def dice(processed,target,faces):
    if target == 0:
        print(processed)
        return
    for face in range(1,faces+1):
        if face > target:
            continue
        dice(processed+str(face),target-face,faces)

def count_dice(processed,target,faces):
    if target == 0:
        return 1
    acc=0
    for face in range(1,faces+1):
        if face > target:
            continue
        acc += count_dice(processed+str(face),target-face,faces)
    return acc

def dice_path_3(processed,target,faces):
    if target == 0:
        if len(processed) <=3:
            print(processed)
    for face in range(1,faces+1):
        if face > target:
            continue
        dice_path_3(processed+str(face),target-face,faces)

def dice_count_3(processed,target,faces):
    if target == 0:
        if len(processed) <=3:
            return 1
        else:
            return 0
    acc=0
    for face in range(1,faces+1):
        if face > target:
            continue
        acc += dice_count_3(processed+str(face),target-face,faces)
    return acc
print(dice("",5,3))

