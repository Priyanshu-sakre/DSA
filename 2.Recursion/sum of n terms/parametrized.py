def sum1(i, sum=0):
    if i == 0:
        print(sum)
        return
    else:
        sum1(i - 1, sum + i)


sum1(10)
