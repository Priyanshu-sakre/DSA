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
