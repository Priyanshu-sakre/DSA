def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        par_index = partition(arr, low, high)
        quick_sort(arr, low, par_index - 1)
        quick_sort(arr, par_index + 1, high)
        return arr


arr = [64, 25, 12, 22, 11]
high = len(arr) - 1
print(quick_sort(arr, 0, high))
