l1 = [64, 25, 12, 22, 11]


def selection_sort(l1):
    for i in range(len(l1) - 1):
        for j in range(i + 1, len(l1)):
            if l1[j] < l1[i]:
                l1[i], l1[j] = l1[j], l1[i]
    return l1


print(selection_sort(l1))
