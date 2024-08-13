def reverse1(i, arr):
    l1 = len(arr)
    if i <= l1 // 2:
        arr[i], arr[l1 - i - 1] = arr[l1 - i - 1], arr[i]
        reverse1(i + 1, arr)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse1(0, arr))
