# naive
n = 17
str1 = ""
while n != 0:
    a = n % 2
    str1 = str(a) + str1
    n //= 2
print(str1)


# efficient
def binary1(n):
    if n == 0:
        return 0
    return n % 2 + 10 * binary1(n // 2)


print(binary1(17))
