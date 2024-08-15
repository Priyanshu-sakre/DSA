def remove_duplicate(n, arr):
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1
    return i + 1


arr = [1, 2, 2, 2, 3]
n = len(arr)
print(remove_duplicate(n, arr))
