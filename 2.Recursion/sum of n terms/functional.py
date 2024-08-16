def sum1(i):
    if i == 1:
        return 1
    else:
        return i + sum1(i - 1)


print(sum1(10))
