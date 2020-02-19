count=0
def subsequences(processed,unprocessed):
    global count
    if len(unprocessed) ==0 and len(processed)==0:
        count -= 1
    if len(unprocessed)==0:
        count +=1
        print(processed)
        return
    ch = unprocessed[0]
    subsequences(processed+ch,unprocessed[1:])
    subsequences(processed,unprocessed[1:])


def count_subsequences(processed,unprocessed):
    if len(unprocessed) ==0:
        if len(processed)==0:
            return 0
        return 1
    ch = unprocessed[0]
    left = count_subsequences(processed+ch,unprocessed[1:])
    right = count_subsequences(processed,unprocessed[1:])
    return left + right


def ret_subsequences(processed,unprocessed):
    if len(unprocessed) ==0:
        if len(processed)==0:
            return []
        return [processed]
    ch = unprocessed[0]
    acc=[]
    acc.extend(ret_subsequences(processed+ch,unprocessed[1:]))
    acc.extend(ret_subsequences(processed,unprocessed[1:]))
    return acc
print(ret_subsequences("","abc"))
