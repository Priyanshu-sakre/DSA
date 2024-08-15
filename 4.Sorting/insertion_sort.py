l1 = [64, 25, 12, 22, 11]


def insertion_sort(l1):
    for i in range(len(l1)):
        j = i
        while j > 0 and l1[j - 1] > l1[j]:
            l1[j - 1], l1[j] = l1[j], l1[j - 1]
            j -= 1
    return l1


print(insertion_sort(l1))
