def selection_sort(arr, i):
    if i > len(arr) - 2:
        return arr
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
    return selection_sort(arr, i + 1)


arr = [64, 25, 12, 22, 11]
print(selection_sort(arr, 0))
