# parametrized
def sum_digits(n, sum1):
    if n == 0:
        print(sum1)
        return
    a = n % 10
    sum_digits(n // 10, sum1 + a)


sum_digits(253, 0)


# functional
def sum_digits2(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits2(n // 10)


print(sum_digits2(253))
