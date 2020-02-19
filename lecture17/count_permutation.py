def permute(processed,unprocessed):
    if len(unprocessed)==0:
        return 1
    acc=0
    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec_unprocessed = unprocessed[:i] + unprocessed[i+1:]
        acc += permute(processed+ch,rec_unprocessed)
    return acc

def ret_permute(processed,unprocessed):
    if len(unprocessed)==0:
        if len(processed) == 0:
            return []
        return [processed]
    acc=[]
    for i in range(len(unprocessed)):
        ch = unprocessed[i]
        rec_unprocessed = unprocessed[:i] + unprocessed[i+1:]
        acc.extend(ret_permute(processed+ch,rec_unprocessed))
    return acc
print(ret_permute("","abc"))