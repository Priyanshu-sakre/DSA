n = 1345
num = n
count = 0
while num != 0:
    a = num % 10
    count += 1
    num //= 10
print(count)
