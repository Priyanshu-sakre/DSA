def divisors(n):
    list1 = [True] * (n + 1)
    for i in range(2, int(n ** (0.5) + 1)):
        if list1[i]:
            for j in range(2 * i, n + 1, i):
                list1[j] = False
    for i in range(2, n + 1):
        if list1[i]:
            print(i, end=" ")


divisors(23)
