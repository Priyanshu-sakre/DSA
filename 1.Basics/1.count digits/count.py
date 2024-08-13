n = 1345
count = 0
while n != 0:
    a = n % 10
    count += 1
    n //= 10
print(count)
