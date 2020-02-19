def lcs(first, second):

    if (len(first) == 0) or (len(second) == 0):
        return 0

    if first[0] == second[0]:
        return 1 + lcs(first[1:], second[1:])
    else:
        left = lcs(first[1:], second)
        right = lcs(first, second[1:])
        return max(left, right)


def ret_lcs(first, second):

    if (len(first) == 0) or (len(second) == 0):
        return 0, ""

    if first[0] == second[0]:
        total_c, yet = ret_lcs(first[1:], second[1:])
        return total_c + 1, first[0] + yet

    else:
        left_c, left_yet = ret_lcs(first[1:], second)
        right_c, right_yet = ret_lcs(first, second[1:])

        if left_c > right_c:
            return left_c, left_yet
        else:
            return right_c, right_yet


def ret_li_lcs(first, second):
    if (len(first) == 0) or (len(second) == 0):
        return 0, [""]

    if first[0] == second[0]:
        total_c, yet = ret_li_lcs(first[1:], second[1:])
        return total_c + 1, [first[0]+item for item in yet]

    else:
        left_c, left_yet = ret_li_lcs(first[1:], second)
        right_c, right_yet = ret_li_lcs(first, second[1:])

        if left_c > right_c:
            return left_c, left_yet
        elif left_c < right_c:
            return right_c, right_yet
        else:
            return left_c, left_yet + right_yet


max_len, items = ret_li_lcs("manan", "aman")
print(max_len, set(items))