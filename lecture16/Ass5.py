def ntriangle(n):
    if n<=1:
        return n
    return n+ ntriangle(n-1)

print(ntriangle(3))