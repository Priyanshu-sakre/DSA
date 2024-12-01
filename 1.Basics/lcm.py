# naive
a = 4
b = 6
for i in range(1, (a * b) + 1):
    b *= i
    if b % a == 0:
        print(b)
        break
# optimal
"""a * b = lcm * hcf"""
