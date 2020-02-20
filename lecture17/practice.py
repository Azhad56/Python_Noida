def lcs(first,second):
    if len(first) ==0 and len(second)==0:
        return 0,""
    if first[0].lower()==second[0].lower():
        total_c,yet = lcs(first[1:], second[1:])
        return 1 + total_c,first[0]+yet
    else:
        left_c,left_yet = lcs(first[1:],second)
        right_c,right_yet = lcs(first,second[1:])
        if left_c > right_c:
            return left_c,left_yet
        else:
            return right_c,right_yet
print(lcs("man","Man"))