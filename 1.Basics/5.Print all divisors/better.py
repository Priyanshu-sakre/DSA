num = 36
l1 = []
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        l1.append(i)
    if num // i != i:
        l1.append(num // i)
print(sorted(l1))
