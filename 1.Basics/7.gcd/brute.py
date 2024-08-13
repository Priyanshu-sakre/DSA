a = 52
b = 10
for i in range(1, min(a, b)):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)
