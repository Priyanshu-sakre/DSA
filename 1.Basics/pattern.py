num = 5
for i in range(2 * num - 1):
    for j in range(2 * num - 1):
        top = i
        left = j
        right = (2 * num - 2) - j
        down = (2 * num - 2) - i
        print(num - min(min(top, down), min(right, left)), end=" ")
    print()
