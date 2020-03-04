def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)
def fibodp(n,memory):
    if n<2:
        return n
    if memory.get(n):
        return memory.get(n)
    first = fibodp(n-1,memory)
    second = fibodp(n-2,memory)
    total = first + second
    memory[n] = total
    return total
print(fibodp(200,memory={}))