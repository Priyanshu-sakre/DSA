def printer(i, n):
    if i <= n:
        print(i)
        printer(i + 1, n)


printer(1, 10)
