def fib(i):
    if i <= 1:
        return i
    return fib(i - 1) + fib(i - 2)


for i in range(10):
    print(fib(i), end=" ")
