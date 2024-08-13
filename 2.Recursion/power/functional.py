def power1(n, b):
    if b == 0:
        return 1
    else:
        return n * power1(n, b - 1)


print(power1(5, 3))
