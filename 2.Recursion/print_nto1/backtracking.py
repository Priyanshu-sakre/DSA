def printer(i, n):
    if i <= n:
        printer(i + 1, n)
        print(i)


printer(1, 10)
