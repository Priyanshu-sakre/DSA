l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(l1) // 2):
    l1[i], l1[len(l1) - i - 1] = l1[len(l1) - i - 1], l1[i]
print(l1)
