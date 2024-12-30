def insertion_sort(arr, i):
    if i > len(arr) - 1:
        return arr
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
    return insertion_sort(arr, i + 1)


arr = [64, 25, 12, 22, 11]
print(insertion_sort(arr, 0))
