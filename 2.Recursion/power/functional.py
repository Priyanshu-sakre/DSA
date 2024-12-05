# brute
def power1(n, b):
    if b == 0:
        return 1
    else:
        return n * power1(n, b - 1)


print(power1(5, 3))


# better
def power2(n, b):
    if b == 0:
        return 1
    if b < 0:
        n = 1 / n
        b = -b
    temp = power2(n, b // 2)
    temp = temp * temp
    if b % 2 == 0:
        return temp
    else:
        return temp * n


print(power2(2, -2))
