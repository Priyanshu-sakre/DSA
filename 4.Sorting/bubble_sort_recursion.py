def bubble_sort(arr, i):
    if i >= len(arr):
        return arr
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return bubble_sort(arr, i + 1)


arr = [64, 25, 12, 22, 11]
print(bubble_sort(arr, 0))
