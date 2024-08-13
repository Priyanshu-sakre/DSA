def sum1(i):
    if i == 0:
        return 0
    else:
        return i + sum1(i - 1)


print(sum1(10))
