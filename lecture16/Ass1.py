def Question1(n):
    if n==0:
        return
    if n%2 !=0:
        print(n)
    Question1(n-1)
    if n%2==0:
        print(n)
Question1(6)