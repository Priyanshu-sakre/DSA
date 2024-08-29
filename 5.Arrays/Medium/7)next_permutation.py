from typing import List

# better
from itertools import permutations


def next_permutation(arr):
    per_list = []
    per = list(permutations(arr))
    for i in per:
        per_list.append(list(i))
    per_list = sorted(per_list, key=lambda i: i[0])
    for i in range(len(per_list)):
        if per_list.index(arr) < len(per_list) - 1:
            return per_list[i + 1]
        else:
            return per_list[0]


arr = [3, 2, 1]
print(next_permutation(arr))


# optimal
def reverse1(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def next_permutation2(arr: List):
    index1 = -1
    n = len(arr)
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            index1 = i
            break
    if index1 == -1:
        reverse1(arr, 0, n - 1)
        return arr
    for i in range(n - 1, index1-1, -1):
        if arr[i] > arr[index1]:
            arr[i], arr[index1] = arr[index1], arr[i]
            break
    reverse1(arr, index1 + 1, n - 1)
    return arr


print(next_permutation2(arr))
