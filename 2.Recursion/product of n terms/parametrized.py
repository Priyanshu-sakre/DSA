def prod(i, p=1):
    if i == 0:
        print(p)
        return
    else:
        prod(i - 1, p * i)


prod(6)
