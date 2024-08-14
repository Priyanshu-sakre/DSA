l1 = [64, 25, 12, 22, 11]


def bubble_sort(l1):
    n = len(l1)
    for i in range(n):
        swap = False  # to optimize the algorithm
        for j in range(n - i - 1):
            if l1[j] > l1[j + 1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
                swap = True
        if swap == False:
            break
    return l1


print(bubble_sort(l1))
