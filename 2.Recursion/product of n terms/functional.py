def prod(i):
    if i == 1:
        return 1
    else:
        return i * prod(i - 1)


print(prod(6))
