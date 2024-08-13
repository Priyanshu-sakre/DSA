a = 15
b = 5
while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a
if a == 0:
    gcd = b
else:
    gcd = a
print(gcd)
