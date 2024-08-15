l1 = [1, 2, 3, 4, 5]
temp = l1[0]
for i in range(1, len(l1)):
    l1[i - 1] = l1[i]
l1[len(l1) - 1] = temp
print(l1)
